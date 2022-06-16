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
