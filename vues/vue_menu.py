from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box, print
from time import sleep
import os

console = Console()


class Menu():

    @staticmethod
    def retour_menu():
        """ Permet de revenir au menu"""

        console.print('''
                ''')
        console.input(Panel("< Tapez entrer pour retourner au menu > ", style='light_goldenrod2', expand=False))
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def continuer_ou_menu():
        """ Permet de continuer ou de revenir au menu"""

        choix = console.input(Panel("< Vous souhaitez continuer ? > \n"
                              "< oui ou non >", style='light_goldenrod2', expand=False)).capitalize()
        while True:
            try:
                if choix == "Oui":
                    return 1

                if choix == "Non":
                    console.print(Panel("< Très bien, vous allez être redirigé vers le menu > \n",
                                  style='light_goldenrod2', expand=False))
                    sleep(2)
                    break

                else:
                    raise ValueError
            except ValueError:
                console.print(Panel(" ❌ [red bold] Veuillez respecter le format attendu [yellow][ oui ou non ][/][/] ",
                              style="bright_red", expand=False))
                return

    @staticmethod
    def ecran_a_zero():
        """ Efface tout l'affichage de l'écran """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def menu_principal():
        """ Affichage du menu principal de l'application """

        Menu.ecran_a_zero()
        print("""
        """)
        console.rule("[bold cyan]  BIENVENUE AU TOURNOI D'ECHEC  ", style='cyan2')
        print("""
        """)
        table = Table(title=' MENU ', box=box.ROUNDED, show_edge=False,
                      show_lines=True, show_header=False, border_style="grey53")
        table.add_column(" Participants ", justify="left", style="cyan1")
        table.add_row(""),
        table.add_row("[bright_yellow bold ]1.[/] Créer un tournoi")
        table.add_row(""),
        table.add_row("[bright_yellow bold ]2.[/] Ajouter un joueur"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]3.[/] Mise à jour du classement"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]4.[/] Afficher un rapport"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]5.[/] Quitter le programme"),
        table.add_row("")

        console.print(table, justify="center")
        print("""
        """)

        try:
            choix = int(console.input
                        (" [cyan2]Veuillez faire votre choix[/] [bright_yellow](1,2,3,4 ou 5)[/] : "))

            if choix > 1 or choix < 5:
                return choix
            else:
                raise ValueError
        except ValueError:
            print("\n \n")
            console.print(Panel(" ❌ [red bold] Ce choix ne fait pas parti des propositions ![/] ",
                                style="bright_red", expand=False))
            return Menu.menu_principal()
