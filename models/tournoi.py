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
