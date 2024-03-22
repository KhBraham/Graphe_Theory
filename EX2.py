class Graphe:
    def __init__(self, n):
        self.n = n
        self.liste_adjacence = {i: [] for i in range(n)}

    def ajouter_arete(self, u, v):
        self.liste_adjacence[u].append(v)


def demoucron(graph):
    def chercher(u, temps, d, f, pile, composante_connexe):
        temps[0] += 1
        d[u] = temps[0]
        f[u] = temps[0]
        pile.append(u)

        for v in graph.liste_adjacence[u]:
            if d[v] == -1:
                chercher(v, temps, d, f, pile, composante_connexe)
                f[u] = min(f[u], f[v])
            elif v in pile:
                f[u] = min(f[u], d[v])

        if d[u] == f[u]:
            composante_connexe.append([])
            while True:
                w = pile.pop()
                composante_connexe[-1].append(w)
                if w == u:
                    break

    n = graph.n
    d = [-1] * n  # Temps de découverte
    f = [-1] * n  # Temps de finition
    temps = [0]  # Utilisé pour suivre le temps dans la fonction dfs
    pile = []  # Pile pour suivre le chemin actuel dans le parcours
    composantes_connexes = []  # Pour stocker les composantes fortement connexes

    for u in range(n):
        if d[u] == -1:
            composante_connexe = []
            chercher(u, temps, d, f, pile, composante_connexe)
            composantes_connexes.extend(composante_connexe)

    return composantes_connexes


# Exemple d'utilisation
g = Graphe(8)
g.ajouter_arete(0, 1)
g.ajouter_arete(1, 2)
g.ajouter_arete(2, 0)
g.ajouter_arete(1, 3)
g.ajouter_arete(3, 4)
g.ajouter_arete(4, 5)
g.ajouter_arete(5, 3)
g.ajouter_arete(6, 7)

composantes_connexes = demoucron(g)

print("Composantes fortement connexes:")
for composante_connexe in composantes_connexes:
    print(composante_connexe)
