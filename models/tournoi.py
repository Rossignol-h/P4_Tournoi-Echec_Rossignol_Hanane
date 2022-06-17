import datetime
from ast import Str
from tinydb import TinyDB, Query
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))

Tournoi_data = Query()
table_tournois = db.table('tournois')


class Tournoi:

    table_tournois = db.table('tournois')

    def __init__(self, participants=[], nom=Str, lieu=Str, nb_tours=4,
                 control_temps=Str, remarques="aucune remarque"):
        self.id = (len(table_tournois.all())+1)
        self.participants = participants
        self.nom = nom
        self.lieu = lieu
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.nb_tours = nb_tours
        self.tours = []
        self.control_temps = control_temps
        self.remarques = remarques

    def ajout_tours(self, tour):
        self.tours.append(tour)

# 2-serialize the instanciated players[mail documentation] :

    def serialisation(self):
        tournoi_serialisé = {
            "id": self.id,
            "participants": self.participants,
            "nom": self.nom,
            "lieu": self.lieu,
            "date": self.date,
            "nb_tours": self.nb_tours,
            "tours": [],
            "control_temps": self.control_temps,
            "remarques": self.remarques
        }
        self.nom
        for tour in self.tours:
            tournoi_serialisé["tours"].append(tour.serialisation())
        return tournoi_serialisé

    def ajout_tournoi__db(self):
        tournoi_serialisé = self.serialisation()
        table_tournois.insert(tournoi_serialisé)

    def maj_tournoi__db(self):
        tournoi_db = Query()
        table_tournois.update(tournoi_db.id == self.id)

    def recup_id_tournoi(self, nom=str):
        doc = table_tournois.search(Tournoi(nom) == self.nom)
        return doc[0].doc_id

    def liste_tours(self):
        return len(self.liste_tours)
