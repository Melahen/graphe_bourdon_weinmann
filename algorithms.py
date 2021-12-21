import networkx as nx


def glouton(graphe) :
    dico = {}
    for sommet in graphe.nodes() :
        dico[sommet] = graphe.degree[sommet]
    liste_sommet_par_degree_decreasing = sorted(dico.keys(), key = dico.get, reverse = True)

    liste_sommets_colorees = []
    couleur_actuelle = 1
    sommet_actuel = 0

    while len(liste_sommets_colorees) < graphe.number_of_nodes() :
        voisins_colored = False

        for voisin in nx.neighbors(graphe, liste_sommet_par_degree_decreasing[sommet_actuel]) :
            if graphe.nodes[voisin]["Color"] == couleur_actuelle :
                voisins_colored = True
                break
        
        if not voisins_colored :
            graphe.nodes[liste_sommet_par_degree_decreasing[sommet_actuel]]["Color"] = couleur_actuelle
            liste_sommets_colorees.append(liste_sommet_par_degree_decreasing[sommet_actuel])


        sommet_actuel += 1
        
        if sommet_actuel == len(liste_sommet_par_degree_decreasing) :
            sommet_actuel = 0
            couleur_actuelle += 1
            for sommet_colored in liste_sommets_colorees :
                if sommet_colored in liste_sommet_par_degree_decreasing :
                    liste_sommet_par_degree_decreasing.remove(sommet_colored)
