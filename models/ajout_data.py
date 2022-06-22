from tinydb import TinyDB, Query
db = TinyDB('db.json', sort_keys=True, indent=4, separators=(',', ': '))
table_joueurs = db.table('joueurs')
table_tournois = db.table('tournois')


def peupler_db():
    
    """ajout automatique de 10 joueurs et 1 tournoi
     pour peupler la base de données """

    if len(table_joueurs) > 0:
        return
    else:
        table_joueurs.insert_multiple([

            {"id": 1, "nom": "Carlson", "prenom": "Magnus", "genre": "M",
             "date_naissance": "30/11/1990", "rang": 1, "score": 0},

            {"id": 2, "nom": "Harmon", "prenom": "Elisabeth", "genre": "F",
             "date_naissance": "07/11/1979", "rang": 2, "score": 0},

            {"id": 3, "nom": "Dubois", "prenom": "Paul", "genre": "M",
             "date_naissance": "22/08/1981", "rang": 3, "score": 0},

            {"id": 4, "nom": "Mercier", "prenom": "Sandra", "genre": "F",
             "date_naissance": "09/04/1989", "rang": 4, "score": 0},

            {"id": 5, "nom": "Smith", "prenom": "Will", "genre": "M",
             "date_naissance": "25/02/2002", "rang": 5, "score": 0},

            {"id": 6, "nom": "Sparrow", "prenom": "Jack", "genre": "M",
             "date_naissance": "19/09/2000", "rang": 6, "score": 0},

            {"id": 7, "nom": "Curie", "prenom": "Marie", "genre": "F",
             "date_naissance": "18/03/1984", "rang": 7, "score": 0},

            {"id": 8, "nom": "Darmon", "prenom": "Gerard", "genre": "M",
             "date_naissance": "05/02/1978", "rang": 8, "score": 0},

            {"id": 9, "nom": "Halle", "prenom": "Berry", "genre": "F",
             "date_naissance": "27/12/1987", "rang": 9, "score": 0},

            {"id": 10, "nom": "Hanks", "prenom": "Tom", "genre": "M",
             "date_naissance": "07/10/1978", "rang": 10, "score": 0}

        ])

    if len(table_tournois) > 0:
        return
    else:
        table_tournois.insert_multiple([

            {
                "control_temps": "bullet",
                "date": "18/06/2022",
                "id": 1,
                "lieu": "Paris",
                "nb_tours": 4,
                "nom": "Coupe de feu",
                "participants": [
                    {
                        "date_naissance": "30/11/1990",
                        "genre": "M",
                        "id": 1,
                        "nom": "Carlson",
                        "prenom": "Magnus",
                        "rang": 1,
                        "score": 3.5
                    },
                    {
                        "date_naissance": "07/11/1979",
                        "genre": "F",
                        "id": 2,
                        "nom": "Harmon",
                        "prenom": "Elisabeth",
                        "rang": 2,
                        "score": 2.0
                    },
                    {
                        "date_naissance": "22/08/1981",
                        "genre": "M",
                        "id": 3,
                        "nom": "Dubois",
                        "prenom": "Paul",
                        "rang": 3,
                        "score": 2.0
                    },
                    {
                        "date_naissance": "09/04/1989",
                        "genre": "F",
                        "id": 4,
                        "nom": "Mercier",
                        "prenom": "Sandra",
                        "rang": 4,
                        "score": 3.0
                    },
                    {
                        "date_naissance": "25/02/2002",
                        "genre": "M",
                        "id": 5,
                        "nom": "Smith",
                        "prenom": "Will",
                        "rang": 5,
                        "score": 0
                    },
                    {
                        "date_naissance": "19/09/2000",
                        "genre": "M",
                        "id": 6,
                        "nom": "Sparrow",
                        "prenom": "Jack",
                        "rang": 6,
                        "score": 1.5
                    },
                    {
                        "date_naissance": "18/03/1984",
                        "genre": "F",
                        "id": 7,
                        "nom": "Curie",
                        "prenom": "Marie",
                        "rang": 7,
                        "score": 1.5
                    },
                    {
                        "date_naissance": "05/02/1978",
                        "genre": "M",
                        "id": 8,
                        "nom": "Darmon",
                        "prenom": "Gerard",
                        "rang": 8,
                        "score": 2.5
                    }
                ],
                "remarques": "",
                "tours": [
                    {
                        "debut_tour": "18/06/2022 03:17:05",
                        "fin_tour": "18/06/2022 03:17:25",
                        "liste_matchs": [
                            {
                                "gagnant": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_A": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_B": {
                                    "date_naissance": "25/02/2002",
                                    "genre": "M",
                                    "id": 5,
                                    "nom": "Smith",
                                    "prenom": "Will",
                                    "rang": 5,
                                    "score": 0
                                },
                                "nom": "Match 1"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "19/09/2000",
                                    "genre": "M",
                                    "id": 6,
                                    "nom": "Sparrow",
                                    "prenom": "Jack",
                                    "rang": 6,
                                    "score": 1.5
                                },
                                "joueur_A": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "joueur_B": {
                                    "date_naissance": "19/09/2000",
                                    "genre": "M",
                                    "id": 6,
                                    "nom": "Sparrow",
                                    "prenom": "Jack",
                                    "rang": 6,
                                    "score": 1.5
                                },
                                "nom": "Match 2"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "joueur_A": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "joueur_B": {
                                    "date_naissance": "18/03/1984",
                                    "genre": "F",
                                    "id": 7,
                                    "nom": "Curie",
                                    "prenom": "Marie",
                                    "rang": 7,
                                    "score": 1.5
                                },
                                "nom": "Match 3"
                            },
                            {
                                "gagnant": None,
                                "joueur_A": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "joueur_B": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "nom": "Match 4"
                            }
                        ],
                        "nom": "Round 1"
                    },
                    {
                        "debut_tour": "18/06/2022 03:17:25",
                        "fin_tour": "18/06/2022 03:18:02",
                        "liste_matchs": [
                            {
                                "gagnant": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_A": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_B": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "nom": "Match 1"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "joueur_A": {
                                    "date_naissance": "19/09/2000",
                                    "genre": "M",
                                    "id": 6,
                                    "nom": "Sparrow",
                                    "prenom": "Jack",
                                    "rang": 6,
                                    "score": 1.5
                                },
                                "joueur_B": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "nom": "Match 2"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "joueur_A": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "joueur_B": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "nom": "Match 3"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "18/03/1984",
                                    "genre": "F",
                                    "id": 7,
                                    "nom": "Curie",
                                    "prenom": "Marie",
                                    "rang": 7,
                                    "score": 1.5
                                },
                                "joueur_A": {
                                    "date_naissance": "25/02/2002",
                                    "genre": "M",
                                    "id": 5,
                                    "nom": "Smith",
                                    "prenom": "Will",
                                    "rang": 5,
                                    "score": 0
                                },
                                "joueur_B": {
                                    "date_naissance": "18/03/1984",
                                    "genre": "F",
                                    "id": 7,
                                    "nom": "Curie",
                                    "prenom": "Marie",
                                    "rang": 7,
                                    "score": 1.5
                                },
                                "nom": "Match 4"
                            }
                        ],
                        "nom": "Round 2"
                    },
                    {
                        "debut_tour": "18/06/2022 03:18:02",
                        "fin_tour": "18/06/2022 03:18:24",
                        "liste_matchs": [
                            {
                                "gagnant": None,
                                "joueur_A": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_B": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "nom": "Match 1"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "joueur_A": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "joueur_B": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "nom": "Match 2"
                            },
                            {
                                "gagnant": None,
                                "joueur_A": {
                                    "date_naissance": "19/09/2000",
                                    "genre": "M",
                                    "id": 6,
                                    "nom": "Sparrow",
                                    "prenom": "Jack",
                                    "rang": 6,
                                    "score": 1.5
                                },
                                "joueur_B": {
                                    "date_naissance": "18/03/1984",
                                    "genre": "F",
                                    "id": 7,
                                    "nom": "Curie",
                                    "prenom": "Marie",
                                    "rang": 7,
                                    "score": 1.5
                                },
                                "nom": "Match 3"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "joueur_A": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "joueur_B": {
                                    "date_naissance": "25/02/2002",
                                    "genre": "M",
                                    "id": 5,
                                    "nom": "Smith",
                                    "prenom": "Will",
                                    "rang": 5,
                                    "score": 0
                                },
                                "nom": "Match 4"
                            }
                        ],
                        "nom": "Round 3"
                    },
                    {
                        "debut_tour": "18/06/2022 03:18:24",
                        "fin_tour": "18/06/2022 03:18:45",
                        "liste_matchs": [
                            {
                                "gagnant": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_A": {
                                    "date_naissance": "30/11/1990",
                                    "genre": "M",
                                    "id": 1,
                                    "nom": "Carlson",
                                    "prenom": "Magnus",
                                    "rang": 1,
                                    "score": 3.5
                                },
                                "joueur_B": {
                                    "date_naissance": "05/02/1978",
                                    "genre": "M",
                                    "id": 8,
                                    "nom": "Darmon",
                                    "prenom": "Gerard",
                                    "rang": 8,
                                    "score": 2.5
                                },
                                "nom": "Match 1"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "joueur_A": {
                                    "date_naissance": "09/04/1989",
                                    "genre": "F",
                                    "id": 4,
                                    "nom": "Mercier",
                                    "prenom": "Sandra",
                                    "rang": 4,
                                    "score": 3.0
                                },
                                "joueur_B": {
                                    "date_naissance": "19/09/2000",
                                    "genre": "M",
                                    "id": 6,
                                    "nom": "Sparrow",
                                    "prenom": "Jack",
                                    "rang": 6,
                                    "score": 1.5
                                },
                                "nom": "Match 2"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "joueur_A": {
                                    "date_naissance": "18/03/1984",
                                    "genre": "F",
                                    "id": 7,
                                    "nom": "Curie",
                                    "prenom": "Marie",
                                    "rang": 7,
                                    "score": 1.5
                                },
                                "joueur_B": {
                                    "date_naissance": "07/11/1979",
                                    "genre": "F",
                                    "id": 2,
                                    "nom": "Harmon",
                                    "prenom": "Elisabeth",
                                    "rang": 2,
                                    "score": 2.0
                                },
                                "nom": "Match 3"
                            },
                            {
                                "gagnant": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "joueur_A": {
                                    "date_naissance": "22/08/1981",
                                    "genre": "M",
                                    "id": 3,
                                    "nom": "Dubois",
                                    "prenom": "Paul",
                                    "rang": 3,
                                    "score": 2.0
                                },
                                "joueur_B": {
                                    "date_naissance": "25/02/2002",
                                    "genre": "M",
                                    "id": 5,
                                    "nom": "Smith",
                                    "prenom": "Will",
                                    "rang": 5,
                                    "score": 0
                                },
                                "nom": "Match 4"
                            }
                        ],
                        "nom": "Round 4"
                    }
                ]
            }
        ])
