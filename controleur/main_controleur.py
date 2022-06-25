from models.joueur import Joueur, Participants
from models.ajout_data import peupler_db
from models.rapport import RapportModel
from models.tour import Tour, Match
from models.tournoi import Tournoi
# Vues
from vues.vue_tournoi import VueTournoi
from vues.vue_rapport import VueRapport
from vues.vue_joueur import VueJoueur
from vues.vue_tour import VueTour
from vues.vue_menu import Menu

# Library
from datetime import datetime
import sys

now = datetime.now()


class Controleur:
    """Main controller."""

    def __init__(self):
        self.vue_menu = Menu()
        self.vue_rapport = VueRapport()
        self.vue_tournoi = VueTournoi()
        self.vue_tour = VueTour()
        self.vue_joueur = VueJoueur()
        self.models_rapport = RapportModel()
        self.models_joueur = Joueur()
        self.models_participants = Participants()
        self.models_tournoi = Tournoi()

    def execution_programme(self):
        peupler_db()
        while True:
            choix = Menu.menu_principal()

            if choix == 1:
                Controleur.creation_tournoi(self)

            elif choix == 2:
                Controleur.ajout_joueur(self)

            elif choix == 3:
                Controleur.maj_joueurs(self)

            elif choix == 4:
                Controleur.execute_rapport(self)

            elif choix == 5:
                return sys.exit()
            else:
                VueTour.message_erreur()
                return
# ===================================================================== JOUEURS

    def instance_joueur(self):
        prenom = self.vue_joueur.nom(1)
        nom = self.vue_joueur.nom()
        date_naissance = self.vue_joueur.date_naissance()
        genre = self.vue_joueur.genre()
        rang = self.vue_joueur.rang()

        return Joueur(nom, prenom, date_naissance, genre, rang)

    def ajout_joueur(self):
        nouveau_joueur = self.instance_joueur()
        self.vue_joueur.fin_instance()
        return Joueur.ajout_joueur__db(nouveau_joueur)

# ============================================================ MAJ CLASSEMENT JOUEURS

    def maj_rang_joueurs(self, tournoi=None, case=0):
        """ Met à jour le rang des joueurs de son choix
        case == 0 : pour la mise à jour à partir du menu principal
        case !0 : pour la mise à jour à la fin d'un tournoi"""

        if case == 0 and tournoi is None:
            ids = Joueur.liste_db("id")
            rangs = Joueur.liste_db("rang")

        else:
            tournoi = self.models_rapport.import_tournoi(tournoi.id)
            ids = Participants.liste_participants(tournoi, 'id')
            rangs = self.models_participants.liste_participants(tournoi, 'rang')

# = On demande les ids et les nouveaux rang
        VueJoueur.intro_demander_id()
        liste_ids = VueJoueur.demander_ids(ids, 1)
        VueJoueur.intro_demander_rang()
        liste_rangs = VueJoueur.demander_rangs(rangs)

# = Vérifie si le nombre d'ids est differents du nombre de rangs

        while True:
            if len(liste_ids) != len(liste_rangs):
                liste_rangs = VueJoueur.demander_rangs(rangs, 1)
            else:
                Joueur.maj_rangs__db(liste_ids, liste_rangs)
            return VueJoueur.fin_classement()

# ================================================

    def maj_joueurs(self, tournoi=None, case=0):
        """ Gère l'affichage et l'ordre de la mise à jour du rang
            d'un joueur """
        while True:
            Menu.ecran_a_zero()
            self.affiche_joueurs(tournoi, case)
            self.maj_rang_joueurs(tournoi, case)
            self.affiche_joueurs()
            reponse = Menu.continuer_ou_menu()
            if reponse == 1:
                continue
            else:
                return self.execution_programme()

# ====================================================== AFFICHAGE INFOS JOUEURS

    def affiche_joueurs(self, tournoi=None, case=0):
        """ Gère l'affichage du tableau des joueurs
            case == 0 : affiche la liste complète des joueurs de la bd
            case !0 : affiche la liste des 8 participants d'un tournoi """

        if (case == 0) and (tournoi is None):
            joueurs = RapportModel.db_liste_tri(RapportModel.table_joueurs, 'id')
        else:
            tournoi = self.models_rapport.import_tournoi(tournoi.id)
            ids = Participants.liste_participants(tournoi, 'id')
            joueurs = self.models_participants.recup_joueur_id(ids)
            self.vue_rapport.affiche_participants(tournoi)

        return VueRapport.affiche_joueurs(joueurs, 2)

# ===================================================================== CREATION TOURNOIS

    def creation_tournoi(self):
        self.vue_tournoi.titre_tournoi()
        self.affiche_joueurs()

        nouveau_tournoi = self.instance_tournoi()
        Tournoi.ajout_tournoi__db(nouveau_tournoi)

        Menu.ecran_a_zero()
        self.vue_tour.titre_tour()
        self.lancer_tour(nouveau_tournoi)
        self.maj_joueurs(nouveau_tournoi, 1)

# ============================================================= AJOUT PARTICIPANTS

    def ajout_participants(self):
        """ Retourne une liste de participants à un tournoi
            à partir des ids donnés par l'utilisateur"""

        liste_id_db = self.models_joueur.liste_db("id")
        self.vue_tournoi.intro_ajout_joueurs()
        liste_id_joueurs = self.vue_joueur.demander_ids(liste_id_db, 0)

        liste_joueurs_db = self.models_participants.recup_joueur_id(liste_id_joueurs)

        participants = self.models_participants.deserialise_joueurs(liste_joueurs_db)
        return participants

# ============================================================= INSTANCIATION TOURNOI

    def instance_tournoi(self):
        """ Instancie un tournoi"""
        participants = self.ajout_participants()
        nom = self.vue_tournoi.nom_tournoi()
        lieu = self.vue_tournoi.lieu_tournoi()
        nb_tours = self.vue_tournoi.nb_tour()
        control_temps = self.vue_tournoi.control_temps()
        remarques = self.vue_tournoi.remarques()

        return Tournoi(participants, nom, lieu, nb_tours, control_temps, remarques)

# =============================================================== LANCER UN TOUR

    def lancer_tour(self, tournoi):
        """ Lance un tour avec gestion des participants et matchs """
        Participants.ajout_joueurs(tournoi.participants)
        participants = Participants.liste[0]

        for i in range(int(tournoi.nb_tours)):
            if i == 0:
                participants_tri1 = RapportModel.db_liste_tri(participants, 'rang')
                paire_joueurs = Match.match_tour1(participants_tri1)
            else:
                liste_scores = Match.recup_score(paire_joueurs)
                if Match.verifie_doublon(liste_scores):
                    participants_tri2 = RapportModel.db_liste_tri(participants, 'rang')
                else:
                    participants_tri2 = RapportModel.db_liste_tri(participants, 'score')

                paire_joueurs = Match.match_tour_suivant(participants_tri2, tournoi)

            tour = Tour(i+1)

            time = datetime.now()
            tour.debut_timestamp(int(datetime.timestamp(time)))

            for index, paire in enumerate(paire_joueurs, 1):
                tour.ajout_matchs(Match(index, paire[0], paire[1]))

            self.vue_tour.affiche_matchs(tour)

            for match in tour.liste_matchs:
                match.gagnant = self.vue_tour.demander_gagnant(match)
                match.ajout_score()

            time2 = datetime.now()
            tour.fin_timestamp(int(datetime.timestamp(time2)))

            tournoi.ajout_tours(tour)
            tournoi.maj_tournoi__db()

        VueTour.titre_fin_tournoi()

# ================================================================ RAPPORTS

    def execute_rapport(self, choix1=0):
        """ Affiche le menu et les différents rapports """
        Menu.ecran_a_zero()
        while True:
            if choix1 > 0:
                choix = choix1
            else:
                choix = VueRapport.rapport_menu()

            if choix == 1:
                Menu.ecran_a_zero()
                list_joueurs_db = RapportModel.db_liste_tri(RapportModel.table_joueurs, 'nom')
                self.vue_rapport.affiche_joueurs(list_joueurs_db, 0)
                Menu.retour_menu()

            elif choix == 2:
                Menu.ecran_a_zero()
                list_joueurs_db = RapportModel.db_liste_tri(RapportModel.table_joueurs, 'rang')
                self.vue_rapport.affiche_joueurs(list_joueurs_db, 1)
                Menu.retour_menu()

            elif choix == 3:
                Menu.ecran_a_zero()
                list_tournois_db = RapportModel.db_liste_tri(RapportModel.table_tournois, 'id')

                if len(list_tournois_db) == 0:
                    self.vue_rapport.affiche_tournoi(list_tournois_db)
                    Menu.retour_menu()
                else:
                    self.vue_rapport.affiche_tournoi(list_tournois_db)
                    tournoi_id = self.vue_rapport.demander_id_tournoi(list_tournois_db)
                    tournoi = self.models_rapport.import_tournoi(tournoi_id)

                    Menu.ecran_a_zero()
                    self.vue_rapport.affiche_details(tournoi['tours'])
                    self.vue_rapport.affiche_participants(tournoi)
                    Menu.retour_menu()

            elif choix == 4:
                self.execution_programme()

            else:
                # VueTour.message_erreur()
                return
# ============================================================== FIN


controleur = Controleur()


controleur.execution_programme()
