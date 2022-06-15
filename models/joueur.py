from ast import Str
from tinydb import TinyDB, Query
db = TinyDB('db.json', sort_keys=False, indent=3, separators=(',', ': '))


class Joueur():
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

    def serialisation_joueur(self):
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
        joueur_serialisé = self.serialisation_joueur()
        Joueur.db.insert(joueur_serialisé)
