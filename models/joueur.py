from ast import Str
from tinydb import TinyDB, Query
db = TinyDB('db.json', sort_keys=False, indent=3, separators=(',', ': '))


class Joueur():
    """Initialise un joueur """
    db = db.table('joueurs')

    def __init__(self, nom=Str, prenom=Str,
                 date_naissance=Str, genre=Str, rang=0):
        self.id = (len(self.db.all())+1)
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.genre = genre
        self.rang = rang
        self.score = 0.0

    def __str__(self):
        resume_player = f'prenom : {self.prenom} -- rang : {self.rang} -- score : {self.score}'
        return resume_player(self)

# 2-sérialisation des joueurs instancié :

    def serialisation_joueur(self):
        """Sérialise un joueur """
        self.joueur_serialisé = {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'genre': self.genre,
            'rang': self.rang,
            'score': self.score
        }
        return self.joueur_serialisé

# 3- Ajout des joueurs à la base de données :

    def ajout_joueur__db(self):
        """Ajoute le jour serialisé à la base de donnée """
        joueur_serialisé = self.serialisation_joueur()
        Joueur.db.insert(joueur_serialisé)

# 3a- Mise à jour du classement des joueurs dans la base de données :

    @classmethod
    def maj_rangs__db(cls, liste_ids, liste_rangs):
        """Ajoute le jour serialisé à la base de donnée """
        for id, rang in zip(liste_ids, liste_rangs):
            joueur_db = Query()
            cls.db.update({'rang': rang}, joueur_db.id == id)

    @classmethod
    def liste_db(cls, valeur):
        """Récupère une liste de valeur dans la base de donnée
            à partir d'une clé (valeur en paramètre) """
        liste_db = []
        for i in range(len(cls.db)):
            resultat = cls.db.all()[i][str(valeur)]
            liste_db.append(resultat)
        return liste_db

# 4- Récupérer les joueurs de la base de données:

    def recup_joueur_id(self, liste_id_joueurs):
        """Récupère une liste de joueurs dans la base de donnée
            correspondant aux ID donnés en paramètre (liste_id_joueurs) """
        joueurs_db = []
        for (i, element) in enumerate(liste_id_joueurs):
            joueur = self.db.get(doc_id=element)
            joueurs_db.append(joueur)
        return joueurs_db

# 5- les deserialiser :

    def deserialise_joueurs(self, liste):
        """Désérialise la liste de joueurs
        donné en paramètre (liste) """
        joueurs_deserialise = []
        for joueur in liste:
            self.prenom = joueur['prenom']
            self.nom = joueur['nom']
            self.date_naissance = joueur['date_naissance']
            self.genre = joueur['genre']
            self.rang = joueur['rang']
            self.score = joueur['score']
            joueurs_deserialise.append(joueur)

        return joueurs_deserialise


class Participants():
    """Initialise les participants d'un tournoi"""
    liste = []

    @classmethod
    def ajout_joueurs(cls, joueur):
        """Ajoute les joueurs donné en paramètre
        à la liste des participants du tournoi """
        cls.liste.append(joueur)

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


    @staticmethod
    def recup_score(paire_joueurs):
        liste_scores =[]
        for i in range(len(paire_joueurs)):
            match =paire_joueurs[i]
            for a, b in zip(match[::], match[1::2]):
                liste_scores.append([a['score'], b['score']])
        return liste_scores

    @staticmethod
    def verifie_doublon(liste_scores):
        ''' Vérifie la présence de scores dupliqués
           dans chaque matchs'''
        count= 0
        for score in liste_scores:
            if score[0] == score[1]:
                count += 1
            else:
                pass
        if count >=2 :
            return True
        return False

    @staticmethod
    def match_tour_suivant(liste, tournoi):
        """Défini les paires de participants au tournoi
            pour les tours suivants """
        resultat1 = []
        for matchs in tournoi.tours:
            for match in matchs.liste_matchs:
                if (match.joueur_A == liste[0] and match.joueur_B == liste[1]) or (
                    match.joueur_A == liste[1] and match.joueur_B == liste[0]):
                    return [[liste[0], liste[2]],
                            [liste[1], liste[3]],
                            [liste[4], liste[5]],
                            [liste[6], liste[7]]]

        for a, b in zip(liste[::2], liste[1::2]):
            resultat1.append([a, b])
        return resultat1

    @classmethod
    def serialisation(cls):
        """Sérialise la liste de participants """
        joueurs_serialisés = {
            "liste": []
        }
        for joueur in cls.liste1:
            joueurs_serialisés["liste"].append(joueur.serialisation())
        return joueurs_serialisés
