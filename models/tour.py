class Tour():

    def __init__(self, nom, debut_tour=None, fin_tour=None):
        self.nom = ('Round'+'_' + str(nom))
        self.debut_tour = debut_tour
        self.fin_tour = fin_tour
        self.liste_matchs = []

    def __repr__(self):
        return f'nom : {self.nom} -- debut_tour : {self.debut_tour} ' \
               f'fin_tour : {self.fin_tour} '
