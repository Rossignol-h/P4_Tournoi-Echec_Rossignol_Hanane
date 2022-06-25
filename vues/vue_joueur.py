from rich.console import Console
from rich.panel import Panel
from time import sleep
import re

console = Console()

NB_MAX_JOUEURS = 8  # limite maximum de joueurs
LIMITE_RANG = 100  # limite maximum du rang d'un joueur


class VueJoueur:

    # ======================================================= INSTANCIATION D'UN JOUEUR

    def nom(self, case=0):
        regex = "^[A-Z]{1}[a-z]+$"
        if case == 1:
            nom = console.input("\n[cyan2]Veuillez entrer le prénom du joueur[/] : "
                                ).capitalize()
        else:
            nom = console.input("\n[cyan2]Veuillez entrer le nom du joueur[/] : ").capitalize()
        while True:
            try:
                if re.match(regex, nom):
                    return nom
                else:
                    raise ValueError
            except ValueError:
                console.print("")
                console.print(Panel("❌ [bright_red]Desolé vous devez respecter le format"
                                    " merci de reprendre votre saisie[/]",
                                    style="bright_red", expand=False))
            if case == 1:
                return self.nom(1)
            else:
                return self.nom()

    def date_naissance(self):
        regex = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
        date = console.input(
                "\n[cyan2]Veuillez entrer la date de naissance du joueur[/] [ au format [yellow]JJ/MM/AAAA[/] ] : "
            )
        try:
            if re.match(regex, date):
                return date
            else:
                raise ValueError
        except ValueError:
            console.print("")
            console.print(Panel("❌ [bright_red]Desolé vous devez respecter le format"
                                " merci de reprendre votre saisie[/]", style="bright_red",
                                expand=False))
            return self.date_naissance()

    def genre(self):
        genre = console.input(
                "\n[cyan2]Veuillez entrer le genre du joueur[/] (M ou F) : "
            ).upper()

        try:
            if genre == "M" or genre == "F":
                return genre
            else:
                raise ValueError
        except ValueError:
            console.print("")
            console.print(Panel("❌ [bright_red]L'entrée n'est pas valide, veuillez entrer [bright_yellow][ M ou F ][/]"
                                " merci de reprendre votre saisie[/]", style="bright_red",
                                expand=False))
            print("")
            return self.genre()

    def rang(self):
        rang = console.input("\n[cyan2]Veuillez entrer le rang du joueur [yellow](1 à 100)[/][/] : ")
        try:
            rang = int(rang)
            if (rang > 0) or (rang < LIMITE_RANG) and type(rang) == int:
                return rang
            else:
                raise ValueError
        except ValueError:
            console.print(Panel("⚠️ [red bold]Votre saisie n'est pas dans l'intervalle autorisé[/]  ",
                          style="bright_red", expand=False))
            return self.rang()

# ================================================== CHOIX ID POUR MAJ CLASSEMENT

    @staticmethod
    def demander_ids(liste_ids_db, case):
        """ Demande les ID des joueurs
                - soit case == 0 pour ajouter 8 participants au tournoi
                - soit de 1 a 8 joueurs pour mise à jour de leur classement """

        while True:
            try:
                print("")
                ids = list(map(int, console.input(
                      "[cyan2]Veuillez entrer les ID des joueurs de votre choix[/] : "
                    ).split()))

                if case == 0:
                    if (len(ids) < NB_MAX_JOUEURS) or (len(ids) > NB_MAX_JOUEURS):
                        console.print(
                            Panel(
                                f"❌ [bright_red]Desolé vous devez entrer [yellow]{NB_MAX_JOUEURS}[/] joueurs,"
                                " merci de reprendre votre saisie[/]",
                                style="bright_red",
                                expand=False))
                        return VueJoueur.demander_ids(liste_ids_db, int(case))

                else:
                    if (len(ids) <= 0) or (len(ids) > NB_MAX_JOUEURS):
                        console.print(
                            Panel(f" ❌ [bright_red]Desolé vous devez entrer "
                                  f" entre [yellow]1 et {NB_MAX_JOUEURS}[/] joueurs,"
                                  " merci de reprendre votre saisie[/]",
                                  style="bright_red", expand=False))
                        return VueJoueur.demander_ids(liste_ids_db, int(case))

                for id in ids:
                    if id not in liste_ids_db:
                        console.print(
                            Panel(
                                f":thinking_face: [bright_red bold]Desolé l'id [yellow]{id}[/]"
                                " n'existe pas, merci de reprendre votre saisie[/]",
                                style="bright_red",
                                expand=False,
                            )
                        )
                        return VueJoueur.demander_ids(liste_ids_db, int(case))
            except ValueError:
                console.print(
                    Panel(
                        " ❌ [bright_red]Desolé votre saisie n'est pas valide "
                        " merci de respecter le format [/]",
                        style="bright_red",
                        expand=False,
                    )
                )
                return VueJoueur.demander_ids(liste_ids_db, int(case))

            return ids

# ================================================== DEMANDER RANG

    @staticmethod
    def demander_rangs(liste_rangs_db, case=0):
        if case != 0:
            console.print(
                Panel("⚠️ [red bold] Desolé le nombre de rangs saisi ne correspond pas au nombre d'id enregistré [/]",
                      expand=False))
        doublon = []
        while True:
            print("")
            rangs = list(map(int, console.input(
                     "[cyan2]Veuillez entrer votre saisie[/] [yellow](1 à 100)[/] : "
                    ).split()))

            for rang in rangs:
                if rang in liste_rangs_db:
                    doublon.append(rang)

            if len(doublon) >= 1:
                for i in range(len(doublon)):
                    console.print(Panel(f"⚠️ [red bold] le rang [yellow]{doublon[i]}[/]"
                                        " est déjà attribué à un autre joueur ",
                                        style="bright_red", expand=False))
                console.print("""
                    """)
                confirme_rangs = console.input(
                                    "[cyan2] Souhaitez vous confirmer votre choix ?[/] [yellow]( Oui ou Non )[/] : "
                                     ).capitalize()

                if confirme_rangs == "Oui":
                    return rangs
                if confirme_rangs == "Non":
                    return VueJoueur.demander_rangs(liste_rangs_db)

            elif rang < 0 or rang > LIMITE_RANG:
                console.print(Panel(f"⚠️ [red bold]le rang [yellow]{rang}[/] dépasse la limite autorisée[/]  ",
                                    style="bright_red", expand=False))
                return VueJoueur.demander_rangs(liste_rangs_db)

            return rangs

# ================================================================ TITRES, INTRO, MESSAGE

    @staticmethod
    def intro_demander_id():
        console.print("""
        """)
        console.print(
            Panel(
                "Vous pouvez changer le rang de [bold]1 à 8[/] joueurs en entrant leur ID \n "
                " ( dans ce format: 1 2 3 4 ) ", style="light_goldenrod2", expand=False,))

    @staticmethod
    def intro_demander_rang():
        console.print("""
        """)
        console.print(
            Panel(
                "Entrez le nouveau rang de chaque joueur  \n"
                " ( dans ce format: 10 23 31 9 ) ",
                style="light_goldenrod2", expand=False,))

    @staticmethod
    def fin_classement():
        sleep(2)
        console.print("""
        """)
        console.print(
            Panel(
                """Parfait! la mise à jour a été prise en compte [bold pink]:heavy_check_mark: [/]""",
                style="light_green",
                expand=False))
        sleep(1)

    def fin_instance(self):
        sleep(2)
        console.print("""

        """)
        console.print(
            Panel(
                " Parfait ! le joueur a bien été enregistré :heavy_check_mark: ",
                style="light_green",
                expand=False,
            )
        )
        sleep(1)
