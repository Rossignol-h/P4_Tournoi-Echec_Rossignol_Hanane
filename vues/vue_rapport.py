from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box, print
from vues.vue_menu import Menu

console = Console()

NB_MATCHS = 4


class VueRapport:

    @classmethod
    def rapport_menu(cls):
        Menu.ecran_a_zero()
        print("""
        """)
        console.rule("[bold cyan]  RAPPORTS  ", style='cyan2')

        print("""
        """)
        table = Table(title=' MENU ', box=box.ROUNDED, show_edge=False,
                      show_lines=True, show_header=False, border_style="grey53")
        table.add_column(" Participants ", justify="left", style="cyan1")
        table.add_row(""),
        table.add_row("[bright_yellow bold ]1.[/] La liste des joueurs triés par ordre alphabétique")
        table.add_row(""),
        table.add_row("[bright_yellow bold ]2.[/] La liste des joueurs triés selon leur classement"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]3.[/] La liste de tous les tournois ( et leur détails...)"),
        table.add_row(""),
        table.add_row("[bright_yellow bold ]4.[/] Retour au menu principal"),
        table.add_row("")

        console.print(table, justify="center")
        print("""
        """)

        try:
            console.print("""
            """)
            choix = int(console.input
                        (" ⭐️ [cyan2]Veuillez faire votre choix[/] [bright_yellow](1,2,3 ou 4)[/] : "))

            if choix < 1 or choix > 4:
                raise ValueError
            return choix
        except ValueError:
            print("\n Ce choix ne fait pas parti des propositions !\n")
            return VueRapport.rapport_menu()

# ================================================================= TABLEAUX

    @staticmethod
    def affiche_joueurs(liste, case):

        console.print("""
        """)
        console.rule("[bold cyan] LISTE DE TOUS LES JOUEURS ENREGISTRÉS ")
        console.print("""
        """)

        if case == 0:
            table = Table(title=" Les joueurs triés par nom", box=box.ROUNDED)

        elif case == 1:
            table = Table(title=" Les joueurs triés par rang", box=box.ROUNDED)

        else:
            table = Table(title=" Les joueurs triés par ID", box=box.ROUNDED)

        table.add_column(" ID ", justify="center", style="light_goldenrod2")
        table.add_column("Classement", justify="center", style="cyan2", no_wrap=True)
        table.add_column("Joueurs", justify="left", style="cyan")
        table.add_column("Date de naissance", justify="center", style="light_goldenrod2")
        table.add_column("Genre", justify="center", style="green")

        for i in range(len(liste)):
            table.add_row(f'{liste[i]["id"]}', f'{liste[i]["rang"]}', liste[i]["nom"] + ' ' + liste[i]["prenom"],
                          liste[i]["date_naissance"], liste[i]["genre"])

        return console.print(table, justify="center")

    @staticmethod
    def affiche_tournoi(liste):
        table1 = Table(title="liste de tous les tournois", box=box.ROUNDED)

        table1.add_column(" ID ", justify="center", style="yellow")
        table1.add_column("Nom", justify="left", style="green", no_wrap=True)
        table1.add_column("lieu", justify="center", style="cyan")
        table1.add_column("Date", justify="center", style="yellow")
        table1.add_column("Controle de temps", justify="center", style="green")
        table1.add_column("Nombre de tour", justify="center", style="green")

        for i in range(len(liste)):
            table1.add_row(f'{liste[i]["id"]}', liste[i]["nom"], liste[i]["lieu"],
                           liste[i]["date"], liste[i]["control_temps"], f'{liste[i]["nb_tours"]}')

        return console.print(table1, justify="center")

# ============================================================== DETAILS D'UN TOURNOI

    @staticmethod
    def demander_id_tournoi(liste_tournoi):
        liste_id_tournoi = []

        for i in range(len(liste_tournoi)):

            ids = (f'{liste_tournoi[i]["id"]}')
            liste_id_tournoi.append(ids)

        console.print(Panel(" Pour accéder au détails d'un tournoi ", style='light_goldenrod2', expand=False))
        try:
            id = int(console.input
                     ("[cyan2]Veuillez entrer l'ID du tournoi de votre choix : "))

            if str(id) in liste_id_tournoi:
                return id
            raise ValueError
        except ValueError:
            print("Desolé votre saisie n'est pas valide !")
            return VueRapport.demander_id_tournoi(liste_tournoi)

# ============================================================ AFFICHE PARTICIPANTS

    @staticmethod
    def affiche_participants(tournoi):
        participants = tournoi['participants']
        print('')
        table3 = Table(title='LISTE DES PARTICIPANTS', box=box.ROUNDED)
        table3.add_column(" Participants ", justify="left", style="yellow")
        table3.add_column(" Classement ", justify="center", style="cyan")
        table3.add_column(" Score ", justify="left", style="yellow")

        for i in range(len(participants)):
            table3.add_row(participants[i]["prenom"] + ' ' + participants[i]["nom"],
                           f'{participants[i]["rang"]}', f'{participants[i]["score"]}')

        return console.print(table3, justify="center")

# ============================================================== AFFICHE TOURS

    @staticmethod
    def affiche_tours(tournoi):
        tours = tournoi['tours']
        console.print('''
                ''')
        table = Table(title="LISTE DES TOURS", box=box.ROUNDED)

        table.add_column("Nom", justify="left", style="yellow")
        table.add_column(" Début ", justify="center", style="magenta", no_wrap=True)
        table.add_column(" fin ", justify="center", style="blue")

        for i in range(len(tours)):
            table.add_row(f"{tours[i]['nom']}", f"{tours[i]['debut_tour']}", f"{tours[i]['fin_tour']}")

        return console.print(table, justify="center")

# ======================================================================== AFFICHE MATCHS

    @staticmethod
    def affiche_matchs(tournoi):
        tours = tournoi['tours']
        liste_tours = []
        matchs = []
        joueurs_A = []
        joueurs_B = []
        gagnants = []

        for i in range(tournoi['nb_tours']):
            liste_tours.append(tours[i]['liste_matchs'])
            matchs.append(liste_tours[i])
        for x in range(len(tours)):
            for i in range(NB_MATCHS):
                A = f"{matchs[x][i]['joueur_A']['prenom']} {matchs[x][i]['joueur_A']['nom']}"
                B = f"{matchs[x][i]['joueur_B']['prenom']} {matchs[x][i]['joueur_B']['nom']}"

                if matchs[x][i]['gagnant'] is None:
                    gagnants.append('Match nul')
                else:
                    G = f"""{matchs[x][i]['gagnant']['prenom']} {matchs[x][i]['gagnant']['nom']}
                    {matchs[x][i]['gagnant']['score']}"""
                    gagnants.append(G)
                joueurs_A.append(A)
                joueurs_B.append(B)

# ================================================= affiche le tableau des matchs
        print("""
        """)
        table = Table(title='LISTE DES MATCHS', title_style='cyan2', box=box.SIMPLE, show_header=False)
        table.add_column(" JOUEUR A ", justify="center")
        table.add_column(" VS ", justify="center", style="bright_yellow", vertical="middle")
        table.add_column(" JOUEUR B ", justify="center")
        table.add_column(" JOUEUR B ", justify="center")
        table.add_column(" JOUEUR B ", justify="center", vertical="middle")
        table.add_column(" JOUEUR B ", justify="center")

        for joueur_A, joueur_B, gagnant, in zip(joueurs_A, joueurs_B, gagnants):
            table.add_row(
                Panel(f"{joueur_A}", style="dark_slate_gray2", title="joueur A", expand=False),
                "VS",
                Panel(f"{joueur_B}", style="plum2", title="joueur B", expand=False),
                Panel("Qui est le vainqueur ?", style="light_goldenrod2", title="Fin du match", expand=False),
                "==>",
                Panel(f" {gagnant} ", title='[white]Gagnant 🏆', style='light_green', expand=False))

        return console.print(table, justify="center")
