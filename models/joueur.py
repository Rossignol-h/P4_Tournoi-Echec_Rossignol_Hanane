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

    def ajout_joueur__db(self):
        """Ajoute le joueur serialisé à la base de donnée """
        joueur_serialisé = self.serialisation_joueur()
        Joueur.db.insert(joueur_serialisé)

    @classmethod
    def liste_db(cls, clé):
        """Récupère une liste de valeur dans la base de donnée
            à partir d'une clé donnée en paramètre ('ID' ou 'rang') """
        liste_db = []
        for i in range(len(cls.db)):
            resultat = cls.db.all()[i][str(clé)]
            liste_db.append(resultat)
        return liste_db

    @classmethod
    def maj_rangs__db(cls, liste_ids, liste_rangs):
        """Met à jour les classements des joueurs
            dans la base de donnée """
            
        for id, rang in zip(liste_ids, liste_rangs):
            joueur_db = Query()
            cls.db.update({'rang': rang}, joueur_db.id == id)

# ========================================================= PARTICIPANTS D'UN TOURNOI


class Participants():
    """Initialise les participants d'un tournoi"""
    db = db.table('joueurs')
    liste = []

    @classmethod
    def recup_joueur_id(cls, liste_id_joueurs):
        """Récupère une liste de joueurs dans la base de donnée
                correspondant aux ID donnés en paramètre (liste_id_joueurs) """
        joueurs_db = []
        for (i, element) in enumerate(liste_id_joueurs):
            joueur = cls.db.get(doc_id=element)
            joueurs_db.append(joueur)

        return joueurs_db

    @classmethod
    def deserialise_joueurs(cls, liste):
        """Désérialise la liste de joueurs
        donné en paramètre (liste) """
        joueurs_deserialise = []
        for joueur in liste:
            cls.prenom = joueur['prenom']
            cls.nom = joueur['nom']
            cls.date_naissance = joueur['date_naissance']
            cls.genre = joueur['genre']
            cls.rang = joueur['rang']
            cls.score = joueur['score']
            joueurs_deserialise.append(joueur)

        return joueurs_deserialise

    @classmethod
    def ajout_joueurs(cls, joueur):
        """Ajoute les joueurs donné en paramètre
        à la liste des participants du tournoi """
        cls.liste.append(joueur)
