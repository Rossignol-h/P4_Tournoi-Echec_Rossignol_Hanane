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

    def __repr__(self):
        return f' nom : {self.nom} id : {self.id} date : {self.date} ' \
               f'nombre tours : {self.nb_tours} controle temps : {self.control_temps}' \
               f'lieu : {self.lieu} participants : {self.participants} tours : {self.tours}'

    def ajout_tours(self, tour):
        self.tours.append(tour)

    def serialisation(self):
        """Sérialise le tournoi """
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
        """ Ajoute le tournoi à la base de donnée """
        tournoi_serialisé = self.serialisation()
        table_tournois.insert(tournoi_serialisé)

    def maj_tournoi__db(self):
        """ Met à jour le tournoi dans la base de donnée """
        tournoi_db = Query()
        table_tournois.update(self.serialisation(), tournoi_db.id == self.id)
