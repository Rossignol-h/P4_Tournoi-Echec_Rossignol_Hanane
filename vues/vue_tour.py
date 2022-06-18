from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich import print, box
from time import sleep
import datetime
now = datetime.datetime.now()

console = Console()
layout = Layout()


class VueTour:

    @staticmethod
    def affiche_matchs(tour):

        console.print('''


                ''')
        table = Table(title=" VOICI LES MATCHS DE CE TOUR ", box=None, show_header=False)
        table.add_column(justify="left", vertical="middle")
        table.add_column(justify="center", no_wrap=True)
        table.add_column(justify="center", vertical="middle")
        table.add_column(justify="center", no_wrap=True)

        for match in tour.liste_matchs:
            joueur_A = f"{match.joueur_A['prenom']} {match.joueur_A['nom']} score: {match.joueur_A['score']}"
            joueur_B = f"{match.joueur_B['prenom']} {match.joueur_B['nom']} score: {match.joueur_B['score']}"
            rang_A = f"{match.joueur_A['rang']}"
            rang_B = f"{match.joueur_B['rang']}"
            nom = f"{match.nom}"

            table.add_row(f"[white]{nom}[/]",
                          Panel(f"[white]{joueur_A}[/]",
                                padding=(1, 3),
                                style="medium_purple1",
                                title="joueur A",
                                subtitle=f"Rang :{rang_A}",
                                subtitle_align="right",
                                expand=False),
                          ":vs_button:",
                          Panel(f"[white]{joueur_B}",
                                padding=(1, 3),
                                style="medium_spring_green",
                                title="joueur B",
                                subtitle=f"Rang :{rang_B}",
                                subtitle_align="right",
                                expand=False)
                          )

        return console.print(table, justify="center")

# =========================================================================================================

    @staticmethod
    def demander_gagnant(match):
        joueur_A = f"{match.joueur_A['prenom']} {match.joueur_A['nom']} {match.joueur_A['score']}"
        joueur_B = f"{match.joueur_B['prenom']} {match.joueur_B['nom']} {match.joueur_B['score']}"

        sleep(1)
        console.print('''
                ''')
        table3 = Table(title='', box=box.SIMPLE, show_header=False)
        table3.add_column(" JOUEUR A ", justify="center")
        table3.add_column(" VS ", justify="center", style="bright_yellow", vertical="middle")
        table3.add_column(" JOUEUR B ", justify="center")

        table3.add_row(Panel(f"{joueur_A}", style="cornflower_blue", title="joueur A", expand=False),
                       "VS",
                       Panel(f"{joueur_B}", style="medium_spring_green", title="joueur B", expand=False))

        console.print(table3, justify="left")

        try:
            sleep(1)
            console.print('''
                ''')

            console.rule("[bold cyan] LORSQUE CE MATCH SERA FINI "
                         " MERCI DE SAISIR LE RESULTAT :  ", align="left")

            table3 = Table(title='', box=box.SIMPLE, show_header=False)
            table3.add_column(" JOUEUR A ", justify="center")
            table3.add_row(Panel(f"{joueur_A}", style="cornflower_blue", title="joueur A", expand=False))
            console.print(table3, justify="left")

            gagnant = str(console.input
                          ("""[cyan2]Le joueur A est : le gagnant 🎉 ( Entrer G ), le perdant 😒 (entrer P )
                ou les joueurs ont fait match nul 😐 (Entrer N )[/] : """)).upper()

            if gagnant != "G" and gagnant != "P" and gagnant != "N":
                raise ValueError

            sleep(1)
            console.print('''
                ''')
            console.print(Panel("""Super! Le résultat à bien été enregistré :heavy_check_mark:""",
                          style='light_goldenrod2', expand=False))

            if gagnant == "G":
                return match.joueur_A
            elif gagnant == "P":
                return match.joueur_B
            elif gagnant == "N":
                return None
        except ValueError:
            print("L'entrée n'est pas valide veuillez entrer (G, P ou N) !")
            return VueTour.demander_gagnant(match)

# ================================================================ TITRES

    @staticmethod
    def titre_tour():
        console.rule("[bold cyan]  LE TOURNOI D'ECHEC COMMENCE  ")

# ================================================================= MESSAGE FIN TOURNOI

    @staticmethod
    def titre_fin_tournoi():
        console.print(Panel("""[white]Ce tournoi est terminé, merci à tous les participants 💖
        Vous allez être redirigé vers le menu principal[/]
        """, style='bright_magenta', expand=False))
        sleep(3)
