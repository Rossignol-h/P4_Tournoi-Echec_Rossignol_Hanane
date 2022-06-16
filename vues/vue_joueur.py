from rich.console import Console
from vues.vue_menu import Menu
from rich.panel import Panel
from time import sleep

console = Console()

NB_MAX_JOUEURS = 8  # limite maximum de joueurs
LIMITE_RANG = 100  # limite maximum du rang d'un joueur


class VueJoueur:

    # ======================================================= INSTANCIATION D'UN JOUEUR

    def prenom(self):
        prenom = console.input(
            "\n[cyan2]Veuillez entrer le prénom du joueur[/] : "
        ).capitalize()
        try:
            if len(prenom) <= 2:
                raise ValueError("le prénom est trop court !")
            return prenom
        except Exception as e:
            print(e)
            return self.prenom()

    def nom(self):
        nom = console.input(
            "\n[cyan2]Veuillez entrer le nom du joueur[/] : "
        ).capitalize()
        try:
            if len(nom) <= 2:
                raise ValueError("le nom est trop court !")
            return nom
        except Exception as e:
            print(e)
            return self.nom()

    def date_naissance(self):
        date = str(
            console.input(
                "\n[cyan2]Veuillez entrer la date de naissance du joueur[/] (au format JJ/MM/AAAA) : "
            )
        )

        try:
            if len(date) <= 2:
                raise ValueError("la date n'est pas valide !")
            return date
        except Exception as e:
            print(e)
        return self.date_naissance()

    def genre(self):
        try:
            genre = console.input(
                "\n[cyan2]Veuillez entrer le genre du joueur[/] (M ou F) : "
            ).upper()

            if genre != "M" and genre != "F":
                raise ValueError
            return genre
        except ValueError:
            print("L'entrée n'est pas valide, veuillez entrer 'M' ou 'F'")
            return self.genre()

    def rang(self):
        rang = int(console.input(
            "\n[cyan2]Veuillez entrer le rang du joueur[/] : "))
        try:
            if rang <= 0:
                raise ValueError("Le rang ne peut être inférieur a 0")
            return rang
        except ValueError:
            print("Desolé, l'entrée n'est pas valide !")
            return self.rang()
