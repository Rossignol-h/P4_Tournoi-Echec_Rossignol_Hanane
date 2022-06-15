from tinydb import TinyDB, Query

db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
table_joueurs = db.table('joueurs')
table_tournois = db.table('tournois')


class RapportModel:
    table_joueurs = db.table('joueurs')
    table_tournois = db.table('tournois')

    @classmethod
    def liste_complete(cls, table):
        return table.all()
