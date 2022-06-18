from models.rapport import RapportModel
from models.joueur import Joueur, Participants
from models.tournoi import Tournoi
from models.tour import Tour, Match
from models.ajout_data import peupler_db
# Vues
from vues.vue_menu import Menu
from vues.vue_rapport import VueRapport
from vues.vue_tournoi import VueTournoi
from vues.vue_tour import VueTour
from vues.vue_joueur import VueJoueur

# Library
import sys
from datetime import datetime
from tinydb import TinyDB, Query
db = TinyDB("db.json")
now = datetime.now()
NB_PARTICIPANTS = 8


class Contrôleur:
    """Main controller."""

    def __init__(self):
        self.vue_menu = Menu()
        self.vue_rapport = VueRapport()
        self.vue_tournoi = VueTournoi()
        self.vue_tour = VueTour()
        self.vue_joueur = VueJoueur()
        self.models_rapport = RapportModel()
        self.models_joueur = Joueur()
        self.models_tournoi = Tournoi()

    def execution_programme(self):
        peupler_db()
        while True:
            choix = Menu.menu_principal()

            if choix == 1:
                Contrôleur.creation_tournoi(self)

            elif choix == 2:
                Contrôleur.ajout_joueur(self)

            elif choix == 3:
                Contrôleur.maj_classement(self)

            elif choix == 4:
                Contrôleur.execute_rapport(self)

            elif choix == 5:
                return sys.exit()
            else:
                VueTour.message_erreur()
                return
# ===================================================================== JOUEURS

    def instance_joueur(self):
        prenom = self.vue_joueur.prenom()
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

    def maj_classement(self):
        Menu.ecran_a_zero()
        self.affiche_joueurs()

        liste_id_db = self.models_joueur.liste_db("id")
        self.vue_joueur.intro_demander_id()
        liste_ids = self.vue_joueur.demander_ids(liste_id_db, 1)

        liste_rang_db = self.models_joueur.liste_db("rang")
        self.vue_joueur.intro_demander_rang()
        liste_rangs = self.vue_joueur.demander_rangs(liste_rang_db)

        self.models_joueur.maj_rangs__db(liste_ids, liste_rangs)
        self.vue_joueur.fin_classement()
        self.affiche_joueurs()

        Menu.retour_menu()

    def affiche_joueurs(self):
        joueurs_db = RapportModel.liste_complete(RapportModel.table_joueurs)
        joueurs = RapportModel.tri_par_id(joueurs_db)
        return self.vue_rapport.affiche_joueurs(joueurs, 2)

# ===================================================================== CREATION TOURNOIS

    def creation_tournoi(self):
        self.vue_tournoi.titre_tournoi()

# ====== 1 - afficher la liste de tous les joueurs enregistrés trié par id :
        self.affiche_joueurs()

# ====== 2 - instance du tournoi :
        nouveau_tournoi = self.instance_tournoi()

# ====== 3 - sauvegarde du tournoi dans la base de données :
        Tournoi.ajout_tournoi__db(nouveau_tournoi)

# ====== 4 - Lancer un tour :
        Menu.ecran_a_zero()
        self.vue_tour.titre_tour()
        self.lancer_tour(nouveau_tournoi)

# ============================================================= AJOUT PARTICIPANTS

    def ajout_participants(self):

        liste_id_db = self.models_joueur.liste_db("id")
        self.vue_tournoi.intro_ajout_joueurs()
        liste_id_joueurs = self.vue_joueur.demander_ids(liste_id_db, 0)

# ====== 2 - recup de la base de données les infos de chaque joueurs :
        liste_joueurs_db = self.models_joueur.recup_joueur_id(liste_id_joueurs)

# ====== 3 - Puis les déserialiser :
        participants = self.models_joueur.deserialise_joueurs(liste_joueurs_db)
        return participants

# ====== 4 - Instancier le tournoi :

    def instance_tournoi(self):
        participants = self.ajout_participants()
        nom = self.vue_tournoi.nom_tournoi()
        lieu = self.vue_tournoi.lieu_tournoi()
        nb_tours = self.vue_tournoi.nb_tour()
        control_temps = self.vue_tournoi.control_temps()
        remarques = self.vue_tournoi.remarques()

        return Tournoi(participants, nom, lieu, nb_tours, control_temps, remarques)

# =============================================================== LANCER UN TOUR

    def lancer_tour(self, tournoi):
        Participants.ajout_joueurs(tournoi.participants)
        participants = Participants.liste[0]

        # ====== 1 - selon le nombre de round :
        for i in range(int(tournoi.nb_tours)):
            if i == 0:
                participants_tri = RapportModel.tri_par_rang(participants)
                paire_joueurs = Participants.match_tour1(participants_tri)
            else:
                liste_scores = Participants.recup_score(paire_joueurs)
                print(liste_scores)
                if Participants.verifie_doublon(liste_scores):
                    participants_tri = RapportModel.tri_par_rang(participants)

                else:
                    participants_tri = RapportModel.tri_par_score(participants)

                paire_joueurs = Participants.match_tour_suivant(participants_tri, tournoi)

            tour = Tour(i+1)

            time = datetime.now()
            tour.debut_timestamp(int(datetime.timestamp(time)))

            for index, paire in enumerate(paire_joueurs, 1):
                tour.ajout_matchs(Match(index, paire[0], paire[1]))
            self.vue_tour.affiche_matchs(tour)

            for match in tour.liste_matchs:

                match.gagnant = self.vue_tour.demander_gagnant(match)
                if match.gagnant is None:

                    match.joueur_A['score'] += float(0.5)
                    match.joueur_B['score'] += float(0.5)
                else:
                    match.gagnant['score'] += float(1)

            time2 = datetime.now()
            tour.fin_timestamp(int(datetime.timestamp(time2)))

            tournoi.ajout_tours(tour)
            tournoi.maj_tournoi__db()

# ================================================== FIN DU TOURNOI

        VueTour.titre_fin_tournoi()
        return self.execution_programme()

# ================================================================ RAPPORTS

    def execute_rapport(self):
        Menu.ecran_a_zero()
        while True:
            choice = VueRapport.rapport_menu()

            if choice == 1:
                Menu.ecran_a_zero()
                list_joueurs_db = RapportModel.tri_par_nom(RapportModel.table_joueurs)
                self.vue_rapport.affiche_joueurs(list_joueurs_db, 0)
                Menu.retour_menu()

            elif choice == 2:
                Menu.ecran_a_zero()
                list_joueurs_db = RapportModel.tri_par_rang(RapportModel.table_joueurs)
                self.vue_rapport.affiche_joueurs(list_joueurs_db, 1)
                Menu.retour_menu()

            elif choice == 3:
                Menu.ecran_a_zero()
                list_tournois_db = RapportModel.tri_par_id(RapportModel.table_tournois)

                if len(list_tournois_db) == 0:
                    self.vue_rapport.affiche_tournoi(list_tournois_db)
                    Menu.retour_menu()
                else:
                    self.vue_rapport.affiche_tournoi(list_tournois_db)
                    tournoi_id = self.vue_rapport.demander_id_tournoi(list_tournois_db)
                    tournoi = self.models_rapport.import_tournoi(tournoi_id)

                    self.vue_rapport.affiche_participants(tournoi)
                    self.vue_rapport.affiche_tours(tournoi['tours'])
                    self.vue_rapport.affiche_matchs(tournoi['tours'])

                    Menu.retour_menu()

            elif choice == 5:
                Contrôleur.execution_programme(self)

            else:
                # VueTour.message_erreur()
                return


# ============================================================== FIN

controller = Contrôleur()


controller.execution_programme()
