class Graphe:
    def __init__(self, n):
        self.n = n
        self.liste_adjacence = {i: [] for i in range(n)}

    def ajouter_arete(self, sommet1, sommet2):
        self.liste_adjacence[sommet1].append(sommet2)
        self.liste_adjacence[sommet2].append(sommet1)

    def colorier_graphe(self):
        sommets_decroissant = sorted(range(self.n), key=lambda x: len(self.liste_adjacence[x]), reverse=True)
        couleurs = [-1] * self.n


        def est_couleur_valide(sommet, couleur):
            return all(couleurs[voisin] != couleur for voisin in self.liste_adjacence[sommet])


        for sommet in sommets_decroissant:
            couleurs_disponibles = set(range(self.n))

            for voisin in self.liste_adjacence[sommet]:
                if couleurs[voisin] in couleurs_disponibles:
                    couleurs_disponibles.remove(couleurs[voisin])


            for couleur in couleurs_disponibles:
                if est_couleur_valide(sommet, couleur):
                    couleurs[sommet] = couleur
                    break


        for sommet, couleur in enumerate(couleurs):
            print(f"Sommet {sommet} de couleur {couleur}")


graphe = Graphe(5)

graphe.ajouter_arete(0, 1)
graphe.ajouter_arete(0, 2)
graphe.ajouter_arete(1, 3)
graphe.ajouter_arete(2, 3)
graphe.ajouter_arete(3, 4)


graphe.colorier_graphe()
