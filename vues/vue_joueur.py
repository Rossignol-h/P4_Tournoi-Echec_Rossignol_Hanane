from rich.console import Console
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
        rang = int(console.input("\n[cyan2]Veuillez entrer le rang du joueur[/] : "))
        try:
            if rang <= 0:
                raise ValueError("Le rang ne peut être inférieur a 0")
            return rang
        except ValueError:
            print("Desolé, l'entrée n'est pas valide !")
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
                                expand=False,
                            )
                        )
                        return VueJoueur.demander_ids(liste_ids_db, int(case))

                else:
                    if (len(ids) <= 0) or (len(ids) > NB_MAX_JOUEURS):
                        console.print(
                            Panel(
                                f"""❌ [bright_red]Desolé vous devez entrer
                                entre [yellow]1 et{NB_MAX_JOUEURS}[/] joueurs, merci de reprendre votre saisie[/]""",
                                style="bright_red",
                                expand=False,
                            )
                        )
                        return VueJoueur.demander_ids(liste_ids_db, int(case))

                for id in ids:
                    if id not in liste_ids_db:
                        console.print(
                            Panel(
                                f":thinking_face: [bright_red bold]Desolé l'id [yellow]{id}[/]"
                                f" n'existe pas, merci de reprendre votre saisie[/]",
                                style="bright_red",
                                expand=False,
                            )
                        )
                        return VueJoueur.demander_ids(liste_ids_db, int(case))
            except ValueError:
                console.print(
                    Panel(
                        "❌ [bright_red]Desolé votre saisie n'est pas valide "
                        " merci de respecter le format [/]",
                        style="bright_red",
                        expand=False,
                    )
                )
                return VueJoueur.demander_ids(liste_ids_db, int(case))
            return ids

# ================================================== DEMANDER RANG

    @staticmethod
    def demander_rangs(liste_rangs_db):
        doublon = []
        while True:
            print("")
            rangs = list(map(int, console.input(
                     "[cyan2]Veuillez entrer votre saisie[/] [yellow](1 à 100)[/] : "
                    ).split()))

            for rang in rangs:
                if rang in liste_rangs_db:
                    doublon.append(rang)

                    if len(doublon) == 1:
                        console.print(
                            Panel(
                                f"⚠️ [red bold] le rang {doublon[0]} est déjà attribué à un autre joueur[/]",
                                expand=False,
                            )
                        )
                        confirme_rang = console.input(
                            "[cyan2] Souhaitez vous confirmer votre choix ?[/] [yellow]( Oui ou Non )[/] : "
                        ).capitalize()

                    if len(doublon) > 1:
                        for i in range(len(doublon)):
                            confirme_rangs = console.input(
                                f"""[cyan2]Attention! le rang {doublon[i]} est déjà attribué à un autre joueur,
                                souhaitez vous confirmer votre choix ?[/] [yellow]( Oui ou Non )[/] : """
                            ).capitalize()

                    if confirme_rang or confirme_rangs == "Oui":
                        rangs.append(rang)
                        return rangs
                    if confirme_rang or confirme_rangs == "Non":
                        continue

                elif rang < 0 or rang > LIMITE_RANG:
                    print(
                        f"""
                    Desolé ce {rang} dépasse la limite"""
                    )
                    return VueJoueur.demander_rangs(liste_rangs_db)
            return rangs

# ================================================================ TITRES

    @staticmethod
    def intro_demander_id():
        console.print(
            Panel(
                "Vous pouvez changer le rang de [bold]1 à 8[/] joueurs en entrant leur ID \n "
                "( dans ce format: 1 2 3 4 ) ", style="light_goldenrod2", expand=False,
            )
        )

    @staticmethod
    def intro_demander_rang():
        console.print(
            Panel(
                "Maintenant, entrez le nouveau rang de chaque joueur "
                " ( dans ce format: 10 23 31 9 ) ",
                style="light_goldenrod2", expand=False,
            )
        )

    @staticmethod
    def fin_classement():
        sleep(2)
        console.print("")
        console.print(
            Panel(
                """Parfait! le rang du joueur a été mis à jour :heavy_check_mark:""",
                style="light_goldenrod2",
                expand=False,
            )
        )
        sleep(1)

    def fin_instance(self):
        sleep(2)
        console.print("")
        console.print(
            Panel(
                "Parfait! le joueur a bien été enregistré :heavy_check_mark: ",
                style="light_goldenrod2",
                expand=False,
            )
        )
        sleep(3)
