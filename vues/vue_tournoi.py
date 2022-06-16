from rich.console import Console
from vues.vue_menu import Menu
from rich.panel import Panel
from rich import print
from time import sleep
import datetime
import re
console = Console()

NOMBRE_TOUR = 5
LIMITE_MAX = 500


class VueTournoi:

    def nom_tournoi(self):
        console.print('')
        nom = str(console.input
                  ("[cyan2]Veuillez entrer le nom du tournoi[/] : ")).capitalize()
        try:
            if len(nom) <= 2:
                raise ValueError("Ce nom est trop court ou incorrect")
            return nom
        except Exception as e:
            print(e)
            return self.nom_tournoi()

    @staticmethod
    def lieu_tournoi():
        regex = r"^[A-Za-z]*"
        filtre = re.compile(regex)
        console.print('')
        lieu = str(console.input
                   ("[cyan2]Veuillez entrer le lieu du tournoi[/] : ")).capitalize()
        while filtre.search(lieu) is None or len(lieu) <= 0:
            lieu = str(console.input
                       ("[cyan2]Veuillez entrer le lieu du tournoi[/] : ")).capitalize()
        return lieu

    @staticmethod
    def date_tournoi():
        while True:
            console.print('')
            date = str(console.input
                       ("[cyan2]'Veuillez entrer la date du tournoi au format JJ/MM/AAAA[/] : ")).upper()
            try:
                date = datetime.datetime.strptime(date, "%d/%m/%Y")
                break
            except ValueError:
                print("Veuillez entrer une date valide au format JJ/MM/AAAA ")
        return date

        # récupération du nom du round
    @staticmethod
    def nb_tour():
        try:
            console.print('')
            nb_tour = int(console.input(
                f"""[cyan2]Veuillez entrer le nombre de tour un chiffre de 1 à {NOMBRE_TOUR}
                (4 par défaut ) : """))

            if nb_tour < 1 or nb_tour > NOMBRE_TOUR:
                raise ValueError
            return nb_tour
        except ValueError:
            print(
                f"Le chiffre n'est pas dans l'intervalle 1 à {NOMBRE_TOUR} !")
            return VueTournoi.nb_tour()

    @staticmethod
    def control_temps():
        try:
            console.print('')
            control_temps = str(console.input(
                "[cyan2]Veuillez entrer le controle de temps (bullet, blitz ou rapide ?)[/] : "
            )
            ).lower()

            if control_temps == "bullet" or control_temps == "blitz" or control_temps == "rapide":
                return control_temps
            else:
                raise ValueError
        except ValueError:
            print("""
                Desolé votre saisie n'est pas valide ! """)
            return VueTournoi.control_temps()

    @staticmethod
    def remarques():
        try:
            remarques = str(console.input(f"""[cyan2]
            Avez vous des remarques à ajouter ?
            (si oui: merci de ne pas dépasser {LIMITE_MAX} caractères)
            (Sinon : tapez entrer)[/] : """)).lower()

            if len(remarques) > LIMITE_MAX:
                raise ValueError
            return remarques
        except ValueError:
            print("Desolé vous avez dépassé la limite autorisée !")
            return VueTournoi.remarques()
