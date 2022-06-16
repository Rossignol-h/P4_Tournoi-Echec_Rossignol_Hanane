from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box, print
import os

console = Console()


class Menu():

    @staticmethod
    def continuer():
        pass

    @staticmethod
    def retour_menu():
        console.print('''
                ''')
        console.input(Panel("< Tapez entrer pour retourner au menu > ",
                      style='light_goldenrod2', expand=False))
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def ecran_a_zero():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def menu_principal():
        Menu.ecran_a_zero()
        console.rule(
            "[bold cyan]  BIENVENUE AU TOURNOI D'ECHEC  ", style='magenta')
        print("""
        """)
        table = Table(title=' MENU ', box=box.ROUNDED, show_header=False)
        table.add_column(" Participants ", justify="left", style="yellow")
        table.add_row(""),
        table.add_row("1. Créer un tournoi")
        table.add_row("2. Ajouter un joueur"),
        table.add_row("3. Mise à jour du classement"),
        table.add_row("4. Afficher un rapport"),
        table.add_row("5. Quitter le programme"),
        table.add_row("")

        console.print(table, justify="center")
        print("""
        """)

        try:
            choix = int(console.input
                        ("[cyan2]Veuillez faire votre choix [/] (1,2,3,4 ou 5) : "))

            if choix < 1 or choix > 5:
                raise ValueError
            return choix
        except ValueError:
            print("\n Ce choix ne fait pas parti des propositions !\n")
        return Menu.menu_principal()
