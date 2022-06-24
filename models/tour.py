from datetime import datetime
now = datetime.now()


class Tour():

    def __init__(self, nom, debut_tour=None, fin_tour=None):
        self.nom = ('Round'+' ' + str(nom))
        self.debut_tour = debut_tour
        self.fin_tour = fin_tour
        self.liste_matchs = []

    def __repr__(self):
        return f'nom du tour : {self.nom} debut du tour : {self.debut_tour} ' \
               f'fin du tour : {self.fin_tour} liste des matchs : {self.liste_matchs}'

    def ajout_matchs(self, match):
        """ Ajoute un match unique
        à la liste de matchs """
        self.liste_matchs.append(match)

    def debut_timestamp(self, timestamp):
        """ Marque le début du tour à partir
        du timestamp donné en paramètre """
        convert = datetime.fromtimestamp(timestamp)
        self.debut_tour = convert.strftime("%d/%m/%Y %H:%M:%S")
        return self.debut_tour

    def fin_timestamp(self, timestamp):
        """ Marque la fin du tour à partir
        du timestamp donné en paramètre """
        convert = datetime.fromtimestamp(timestamp)
        self.fin_tour = convert.strftime("%d/%m/%Y %H:%M:%S")
        return self.fin_tour

    def serialisation(self):
        """ Sérialise un tour """
        tour_serialisé = {
            "nom": self.nom,
            "debut_tour": str(self.debut_tour),
            "fin_tour": str(self.fin_tour),
            "liste_matchs": [],
        }
        for match in self.liste_matchs:
            tour_serialisé["liste_matchs"].append(match.serialisation())
        return tour_serialisé

# ============================================================== MATCH UNIQUE


class Match():
    """ Initialise un match avec une paire
    de participants au tournoi """
    def __init__(self, nom, joueur_A, joueur_B):
        self.nom = ('Match'+' ' + str(nom))
        self.joueur_A = joueur_A
        self.joueur_B = joueur_B
        self.gagnant = None

    def __repr__(self):
        return f' nom : {self.nom} joueur A : {self.joueur_A} joueur B : {self.joueur_B} ' \
               f'gagnant : {self.gagnant} '

    def initialise_gagnant(self, gagnant):
        self.gagnant = gagnant

    @staticmethod
    def match_tour1(liste):
        """Defini les paires de participants
        du premier tour selon le tournoi suisse """
        half = int((len(liste)/2))
        liste1 = liste[:half:]
        liste2 = liste[half::]
        resultat = []

        for a, b in zip(liste1, liste2):
            resultat.append([a, b])
        return resultat

    def ajout_score(self):
        if self.gagnant is None:
            self.joueur_A['score'] += float(0.5)
            self.joueur_B['score'] += float(0.5)

        else:
            self.gagnant['score'] += float(1)

    @staticmethod
    def recup_score(paire_joueurs):
        """ Récupère les scores des participants """
        liste_scores = []
        for i in range(len(paire_joueurs)):
            match = paire_joueurs[i]
            for a, b in zip(match[::], match[1::2]):
                liste_scores.append([a['score'], b['score']])
        return liste_scores

    @staticmethod
    def verifie_doublon(liste_scores):
        ''' Vérifie la présence de scores dupliqués
           dans chaque matchs'''
        count = 0
        for score in liste_scores:
            if score[0] == score[1]:
                count += 1
            else:
                pass
        if count >= 2:
            return True
        return False

    @staticmethod
    def match_tour_suivant(liste, tournoi):
        """Défini les paires de participants au tournoi
            pour les tours suivants """
        paire_tour_suivant = []
        for matchs in tournoi.tours:
            for match in matchs.liste_matchs:
                if (match.joueur_A == liste[0] and match.joueur_B == liste[1]) or (
                        match.joueur_A == liste[1] and match.joueur_B == liste[0]):
                    return [[liste[0], liste[2]],
                            [liste[1], liste[3]],
                            [liste[4], liste[5]],
                            [liste[6], liste[7]]]

        for a, b in zip(liste[::2], liste[1::2]):
            paire_tour_suivant.append([a, b])
        return paire_tour_suivant

    def serialisation(self):
        """ Sérialise le match """

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
