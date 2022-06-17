from tinydb import TinyDB, Query
from rich.console import Console
from rich import print


console = Console()

db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
table_joueurs = db.table('joueurs')
table_tournois = db.table('tournois')


class RapportModel:
    table_joueurs = db.table('joueurs')
    table_tournois = db.table('tournois')

    @classmethod
    def liste_complete(cls, table):
        return table.all()

    @classmethod
    def total_db(cls, table):
        return len(table.all())

    @classmethod
    def tri_par_nom(cls, table):
        resultat = sorted(
            table, key=lambda k: k['nom'])
        return resultat

    @classmethod
    def tri_par_rang(cls, table):
        resultat = sorted(
            table, key=lambda k: k['rang'], reverse=False)
        return resultat

    @classmethod
    def tri_par_score(cls, table):
        resultat = sorted(
            table, key=lambda k: k['score'], reverse=True)
        return resultat

    @classmethod
    def tri_par_id(cls, table):
        resultat = sorted(
            table, key=lambda k: k['id'], reverse=False)
        return resultat

    @classmethod
    def import_tournoi(cls, id):
        query = Query()
        resultat = table_tournois.search(query.id == id)
        tournoi = resultat[0]
        return tournoi

    @classmethod
    def maj_rang_joueurs(cls, tournoi):
        participants = tournoi['participants']
        nouveau_rang = []
        id_joueur = []

        for i in range(len(participants)):
            id = participants[i]["id"]
            rang = participants[i]["rang"]
            id_joueur.append(id)
            nouveau_rang.append(rang)

            for id, rang in zip(id_joueur, nouveau_rang):
                joueur_db = Query()
                cls.table_joueurs.update({'rang': rang}, joueur_db.id == id)
