from rich.console import Console
from vues.vue_menu import Menu
from rich.panel import Panel
from rich import print
import re
console = Console()

NOMBRE_TOUR = 5
LIMITE_MAX = 500


class VueTournoi:

    def nom_tournoi(self):
        console.print('')
        regex = "^[A-Z]{1}[a-z]+$"
        nom = (console.input("[cyan2]Veuillez entrer le nom du tournoi[/] : ")).capitalize()
        while True:
            try:
                if re.match(regex, nom):
                    return nom
                else:
                    raise ValueError
            except ValueError:
                console.print("")
                console.print(Panel("❌ [bright_red]Desolé le nom saisi est incorrect"
                                    " merci de reprendre votre saisie[/]",
                                    style="bright_red", expand=False))
                return self.nom_tournoi()

    def lieu_tournoi(self):
        regex = "^[A-Z]{1}[a-z]+$"
        console.print('')
        lieu = (console.input("[cyan2]Veuillez entrer le lieu du tournoi[/] : ")
                ).capitalize()
        while True:
            try:
                if re.match(regex, lieu):
                    return lieu
                else:
                    raise ValueError
            except ValueError:
                console.print("")
                console.print(Panel("❌ [bright_red]Desolé le lieu saisi est incorrect"
                                    " merci de reprendre votre saisie[/]",
                                    style="bright_red", expand=False))
                return self.lieu_tournoi()

    def nb_tour(self):
        regex = "^[1-5]{1}$"
        console.print('')
        nb_tour = (console.input(
            f"""[cyan2]Veuillez entrer le nombre de tour un chiffre de 1 à {NOMBRE_TOUR}
            (4 par défaut ) : """))
        while True:
            try:
                if re.match(regex, nb_tour):
                    return nb_tour
                else:
                    raise ValueError
            except ValueError:
                console.print("")
                console.print(Panel(
                    f"❌ [bright_red]Le chiffre n'est pas dans l'intervalle [bright_yellow]1 à {NOMBRE_TOUR}[/] !"
                    " merci de reprendre votre saisie[/]",
                    style="bright_red", expand=False))
                return self.nb_tour()

    def control_temps(self):
        regex = "^bullet$|^blitz$|^rapide$"
        try:
            console.print('')
            control_temps = (console.input(
                "[cyan2]Veuillez entrer le controle de temps (bullet, blitz ou rapide ?)[/] : "
            )
            ).lower()

            if re.match(regex, control_temps):
                return control_temps
            else:
                raise ValueError
        except ValueError:
            console.print("")
            console.print(Panel("❌ [bright_red]Veuillez respecter le format attendu"
                                " merci de reprendre votre saisie[/]",
                                style="bright_red", expand=False))
            return self.control_temps()

    def remarques(self):
        try:
            remarques = (console.input(f"""[cyan2]
            Avez vous des remarques à ajouter ?
            (si oui: merci de ne pas dépasser {LIMITE_MAX} caractères)
            (Sinon : tapez entrer)[/] : """)).lower()

            if len(remarques) < LIMITE_MAX:
                return remarques
            else:
                raise ValueError
        except ValueError:
            console.print("")
            console.print(Panel("❌ [bright_red]Desolé vous avez dépassé la limite autorisée"
                                " merci de reprendre votre saisie[/]",
                                style="bright_red", expand=False))
            return self.remarques()

# ================================================================ TITRES

    @staticmethod
    def titre_tournoi():
        Menu.ecran_a_zero()
        console.rule("[bold cyan2]  CREATION DU TOURNOI  ", style="dark_turquoise")
        print("""
        """)

    @staticmethod
    def intro_ajout_joueurs():
        console.print(Panel(" Veuillez ajouter 8 joueurs \n"
                            " [ dans ce format: 1 2 3 4 5 6 7 8 ] ",
                            style='light_goldenrod2', expand=False))
