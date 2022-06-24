from tinydb import TinyDB, Query
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))


class RapportModel:
    """ Gère les rapports """
    table_joueurs = db.table('joueurs')
    table_tournois = db.table('tournois')

    @classmethod
    def db_liste_tri(cls, table, clé=str):
        """ Retourne une table de la base de donnée
             triée par la clé donnée en paramètre """
        if clé == 'score':
            resultat = sorted(table, key=lambda k: k[clé], reverse=True)
        else:
            resultat = sorted(table, key=lambda k: k[clé], reverse=False)
        return resultat

    @classmethod
    def import_tournoi(cls, id):
        """ Retourne un tournoi de la base de donnée
        à partir de l'ID donné en paramètre """
        query = Query()
        resultat = cls.table_tournois.search(query.id == id)
        tournoi = resultat[0]
        return tournoi
