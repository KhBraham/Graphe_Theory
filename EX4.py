class Graphe:
    def __init__(self, n):
        self.n = n
        self.liste_adjacence = {i: [] for i in range(n)}

    def ajouter_arete(self, sommet1, sommet2):
        self.liste_adjacence[sommet1].append(sommet2)
        self.liste_adjacence[sommet2].append(sommet1)

def a_un_circuit(graphe, sommet, visite, parent):
    visite[sommet] = True

    for voisin in graphe.liste_adjacence[sommet]:
        if not visite[voisin]:
            if a_un_circuit(graphe, voisin, visite, sommet):
                return True
        elif parent != voisin:
            return True

    return False

def existe_circuit(graphe):
    visite = {i: False for i in range(graphe.n)}

    for sommet in range(graphe.n):
        if not visite[sommet]:
            if a_un_circuit(graphe, sommet, visite, -1):
                return True

    return False

# Exemple d'utilisation
graphe = Graphe(4)
graphe.ajouter_arete(0, 1)
graphe.ajouter_arete(1, 2)
graphe.ajouter_arete(2, 3)
graphe.ajouter_arete(3, 0)

print("Le graphe a un circuit :", existe_circuit(graphe))

class Graphe:
    def __init__(self, vertices):
        self.vertices = vertices
        self.aretes = []

    def ajouter_arete(self, u, v, poids):
        self.aretes.append((u, v, poids))

def trouver_pere(pere, i):
    if pere[i] == i:
        return i
    return trouver_pere(pere, pere[i])

def union(pere, rang, x, y):
    x_pere = trouver_pere(pere, x)
    y_pere = trouver_pere(pere, y)

    if rang[x_pere] < rang[y_pere]:
        pere[x_pere] = y_pere
    elif rang[x_pere] > rang[y_pere]:
        pere[y_pere] = x_pere
    else:
        pere[y_pere] = x_pere
        rang[x_pere] += 1

def kruskal(graph):
    result = []
    graph.aretes = sorted(graph.aretes, key=lambda item: item[2])

    pere = []
    rang = []

    for node in range(graph.vertices):
        pere.append(node)
        rang.append(0)

    i = 0

    while len(result) < graph.vertices - 1:
        u, v, poids = graph.aretes[i]
        i += 1

        x = trouver_pere(pere, u)
        y = trouver_pere(pere, v)

        if x != y:
            result.append((u, v, poids))
            union(pere, rang, x, y)

    return result

# Exemple d'utilisation
g = Graphe(4)
g.ajouter_arete(0, 1, 10)
g.ajouter_arete(0, 2, 6)
g.ajouter_arete(0, 3, 5)
g.ajouter_arete(1, 3, 15)
g.ajouter_arete(2, 3, 4)

resultat = kruskal(g)
print("Arêtes de l'arbre couvrant de poids minimal avec la méthode de Kruskal:")
for u, v, poids in resultat:
    print(f"{u} -> {v} : {poids}")

class GrapheValue:
    def __init__(self, n):
        self.n = n
        self.liste_adjacence = {i: [] for i in range(n)}

    def ajouter_arete(self, sommet1, sommet2, poids):
        self.liste_adjacence[sommet1].append((sommet2, poids))
        self.liste_adjacence[sommet2].append((sommet1, poids))

class Graphe:
    def __init__(self, sommet):
        self.sommet = sommet
        self.liste_adjacence = {i: [] for i in range(sommet)}

    def ajouter_arete(self, u, v, poids):
        self.liste_adjacence[u].append((v, poids))
        self.liste_adjacence[v].append((u, poids))

def prim(graph):
    arbre_couv = []
    visite = set()
    sommet_init = 0


    heap = [(poids, sommet_init, voisin) for voisin, poids in graph.liste_adjacence[sommet_init]]
    heap.sort()
    visite.add(sommet_init)

    while heap:
        poids, u, v = heap.pop(0)

        if v not in visite:
            visite.add(v)
            arbre_couv.append((u, v, poids))
            for voisin, poids_voisin in graph.liste_adjacence[v]:
                if voisin not in visite:
                    heap.append((poids_voisin, v, voisin))
                    heap.sort()

    return arbre_couv

# Exemple d'utilisation
g = Graphe(4)
g.ajouter_arete(0, 1, 10)
g.ajouter_arete(0, 2, 6)
g.ajouter_arete(0, 3, 5)
g.ajouter_arete(1, 3, 15)
g.ajouter_arete(2, 3, 4)

resultat = prim(g)
print("Arêtes de l'arbre couvrant de poids minimal avec la méthode de Prim:")
for u, v, poids in resultat:
    print(f"{u} -> {v} : {poids}")
