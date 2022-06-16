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
