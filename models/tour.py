
from models.joueur import Participants
from datetime import datetime
now = datetime.now()


class Tour():

    def __init__(self, nom, debut_tour=None, fin_tour=None):
        self.nom = ('Round'+'_' + str(nom))
        self.debut_tour = debut_tour
        self.fin_tour = fin_tour
        self.liste_matchs = []

    def __repr__(self):
        return f'nom : {self.nom} -- debut_tour : {self.debut_tour} ' \
               f'fin_tour : {self.fin_tour} '

    def ajout_matchs(self, match):
        self.liste_matchs.append(match)

    def debut_timestamp(self, timestamp):
        convert = datetime.fromtimestamp(timestamp)
        self.debut_tour = convert.strftime("%d/%m/%Y %H:%M:%S")
        return self.debut_tour

    def fin_timestamp(self, timestamp):
        convert = datetime.fromtimestamp(timestamp)
        self.fin_tour = convert.strftime("%d/%m/%Y %H:%M:%S")
        return self.fin_tour

    def serialisation(self):
        tour_serialisé = {
            "nom": self.nom,
            "debut_tour": str(self.debut_tour),
            "fin_tour": str(self.fin_tour),
            "liste_matchs": [],
            }
        for match in self.liste_matchs:
            tour_serialisé["liste_matchs"].append(match.serialisation())
        return tour_serialisé

# ==============================================================


class Match(Participants):

    def __init__(self, nom, joueur_A, joueur_B):
        self.nom = ('Match'+' ' + str(nom))
        self.joueur_A = joueur_A
        self.joueur_B = joueur_B
        self.gagnant = None

    def initialise_gagnant(self, gagnant):
        self.gagnant = gagnant

    def serialisation(self):
        if self.gagnant is None:
            match_serialise = {
                "nom": self.nom,
                "joueur_A": self.joueur_A,
                "joueur_B": self.joueur_B,
                "gagnant": None
            }
        else:
            match_serialise = {
                "nom": self.nom,
                "joueur_A": self.joueur_A,
                "joueur_B": self.joueur_B,
                "gagnant": self.gagnant
            }
        return match_serialise
