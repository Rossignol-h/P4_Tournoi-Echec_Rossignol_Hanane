from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box, print
from vues.vue_menu import Menu

console = Console()

NB_MATCHS = 4
# ================================================================= MENU


class VueRapport:

    @classmethod
    def rapport_menu(cls):
        Menu.ecran_a_zero()
        console.rule("[bold cyan] RAPPORTS ")

        print("""
            """)
        table = Table(title=' MENU ', title_style="bold bright_magenta",
                      box=box.ROUNDED, border_style="sky_blue2", show_header=False)
        table.add_column(" ", justify="left",
                         overflow="ellipsis", style="cyan2")

        table.add_row(""),
        table.add_row(
            "[bright_yellow bold ]1.[/]  La liste des joueurs triés par ordre alphabétique"),
        table.add_row(""),
        table.add_row(
            "[bright_yellow bold ]2.[/]  La liste des joueurs triés selon leur classement"),
        table.add_row(""),
        table.add_row(
            "[bright_yellow bold ]3.[/]  Afficher tous les tournois ( et leur détails...)"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]4.[/]  Retour au menu principal"),
        table.add_row("")

        console.print(table, justify="center")

        try:
            console.print("""
            """)
            choix = int(console.input
                        (" ⭐️ [cyan2]Veuillez faire votre choix[/] [bright_yellow](1,2,3 ou 4)[/] : "))

            if choix < 1 or choix > 4:
                raise ValueError
            return choix
        except ValueError:
            print("\n Ce choix ne fait pas parti des propositions !\n")
            return VueRapport.rapport_menu()

# =============================================== CHOIX 1 ET 2 DU MENU

    @staticmethod
    def affiche_joueurs(liste, case):
        """ Affiche un tableau de tous les joueurs de la base de donnée
                a partir d'une liste, 
                et case permet d' afficher le titre
                correspondant au tri souhaité  """

        console.print("""
        """)
        console.rule("[bold cyan] LISTE DE TOUS LES JOUEURS ENREGISTRÉS ")
        console.print("""
        """)

        if case == 0:
            table = Table(title=" Les joueurs triés par nom", box=box.ROUNDED)

        elif case == 1:
            table = Table(title=" Les joueurs triés par nom", box=box.ROUNDED)

        else:
            table = Table(title=" Les joueurs triés par ID", box=box.ROUNDED)

        #table = Table(title="", box=box.ROUNDED)
        table.add_column(" ID ", justify="center", style="light_goldenrod2")
        table.add_column("Classement", justify="center",
                         style="cyan2", no_wrap=True)
        table.add_column("Joueurs", justify="left", style="cyan")
        table.add_column("Date de naissance", justify="center",
                         style="light_goldenrod2")
        table.add_column("Genre", justify="center", style="green")

        for i in range(len(liste)):
            table.add_row(f'{liste[i]["id"]}', f'{liste[i]["rang"]}', liste[i]["nom"] + ' ' + liste[i]["prenom"],
                          liste[i]["date_naissance"], liste[i]["genre"])

        return console.print(table, justify="center")

# =============================================== CHOIX 3 DU MENU

    @staticmethod
    def affiche_tournoi(liste):
        """ Affiche un tableau de tous les tournois de la base de donnée
                a partir d'une liste """
        table1 = Table(title="liste de tous les tournois", box=box.ROUNDED)

        table1.add_column(" ID ", justify="center", style="yellow")
        table1.add_column("Nom", justify="left", style="green", no_wrap=True)
        table1.add_column("lieu", justify="center", style="cyan")
        table1.add_column("Date", justify="center", style="yellow")
        table1.add_column("Controle de temps", justify="center", style="green")
        table1.add_column("Nombre de tour", justify="center", style="green")

        for i in range(len(liste)):
            table1.add_row(f'{liste[i]["id"]}', liste[i]["nom"], liste[i]["lieu"],
                           liste[i]["date"], liste[i]["control_temps"], f'{liste[i]["nb_tours"]}')

        return console.print(table1, justify="center")
