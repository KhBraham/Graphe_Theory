class Graphe:
    def __init__(self, n):
        self.n = n
        self.matrice_adjacence = [[0] * n for i in range(n)]
        self.liste_adjacence = {j: [] for j in range(n)}

    def ajouter_arc(self, sommet1, sommet2):
        self.matrice_adjacence[sommet1][sommet2] = 1

        self.liste_adjacence[sommet1].append(sommet2)

    def afficher_matrice(self):
        print("La matrice d'adjacence est :")
        for ligne in self.matrice_adjacence:
            print(ligne)

    def afficher_liste(self):
        print("La liste d'adjacence est :")
        for sommet, voisin in self.liste_adjacence.items():
            print(f"Sommets voisins de {sommet} : {voisin}")

    def chemin(self, origine, extremite, m, chemin_actuel=[]):
        chemin_actuel = chemin_actuel + [origine]
        if origine == extremite and len(chemin_actuel) == m + 1:
            print("Le chemin trouvé", chemin_actuel)
        if len(chemin_actuel) <= m:
            for voisin in self.liste_adjacence[origine]:
                if voisin not in chemin_actuel:
                    self.chemin(voisin, extremite, m, chemin_actuel)

    def afficher_circuits(self, sommet, n, chemin_actuel=[]):
        chemin_actuel = chemin_actuel + [sommet]
        if len(chemin_actuel) > n:
            return
        for voisin in self.liste_adjacence[sommet]:
            if voisin not in chemin_actuel or (len(chemin_actuel) == n and voisin == chemin_actuel[0]):
                print("Circuit trouvé :", chemin_actuel)
            self.afficher_circuits(voisin, n, chemin_actuel)


g = Graphe(4)
g.ajouter_arc(0, 1)
g.ajouter_arc(1,3)
g.ajouter_arc(1, 2)
g.ajouter_arc(2, 3)
g.ajouter_arc(3, 0)
g.afficher_matrice()
g.afficher_liste()
g.chemin(0, 3, 3)
for sommet in range(7):
    g.afficher_circuits(sommet, 7)
