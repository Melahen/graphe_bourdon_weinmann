import networkx as nx


def gloutonNaif(graphe) :
    dico = {}
    for sommet in graphe.nodes() :
        dico[sommet] = graphe.degree[sommet]
    liste_sommet_par_degree_decreasing = list(dico.keys())

    liste_sommets_colorees = []
    couleur_actuelle = 1
    sommet_actuel = 0

    while len(liste_sommets_colorees) < graphe.number_of_nodes() :
        voisins_colored = False

        for voisin in nx.neighbors(graphe, liste_sommet_par_degree_decreasing[sommet_actuel]) :
            if graphe.nodes[voisin]["Color"] == couleur_actuelle :
                voisins_colored = True

        
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



def is_possible(graphe, sommet, couleur_a_verifier) :
    for voisin in nx.neighbors(graphe, sommet) :
        if graphe.nodes[voisin]["Color"] == couleur_a_verifier :
            return False
    return True

def solveSudokuHelper(graphe, sommet) :
    
    if (sommet + 1) == len(graphe) :
        if graphe.nodes[sommet]["Color"] == 0 :
            for pigment in range(1, 10) :
                if is_possible(graphe, sommet, pigment) :
                    graphe.nodes[sommet]["Color"] = pigment
        return graphe
    
    if sommet > 80 :
        graphe = solveSudokuHelper(graphe, (sommet % 9) + 1)
        return graphe

    if graphe.nodes[sommet]["Color"] == 0 :
        for pigment in range(1, 10) :
            if is_possible(graphe, sommet, pigment) :
                graphe.nodes[sommet]["Color"] = pigment
                graphe = solveSudokuHelper(graphe, sommet + 9)
                if sudokuChecker(graphe) :
                    return graphe
                graphe.nodes[sommet]["Color"] = 0
    
    else :
        graphe = solveSudokuHelper(graphe, sommet + 9)
    
    return graphe






def sudokuChecker(graphe) :
    for sommet in graphe.nodes :
        for voisin in nx.neighbors(graphe, sommet) :
            if graphe.nodes[voisin]["Color"] == graphe.nodes[sommet]["Color"] :
                return False
    return True


























"""
def solveur_plutot_humain(g) :

    liste_tous_sommets = [sommet for sommet in g.nodes()]
    dico_chaque_sommet = {}
    for sommet in liste_tous_sommets :

        if g.nodes[sommet]["Color"] == 0 :
        
            for sommet_encore in liste_tous_sommets :
                listes_toutes_couleurs_possible = set([g.nodes[sommet]["Color"] for sommet in g.nodes() if g.nodes[sommet]["Color"] != 0])

                for voisin in nx.neighbors(g, sommet_encore) :
                    listes_toutes_couleurs_possible.discard(g.nodes[voisin]["Color"])
                dico_chaque_sommet[sommet_encore] = listes_toutes_couleurs_possible

                if len(dico_chaque_sommet[sommet_encore]) == 1 :
                    g.nodes[sommet_encore]["Color"] = list(dico_chaque_sommet[sommet_encore])[0]



            les_valeurs = []
            for clef in list(dico_chaque_sommet.keys()) :
                les_valeurs.append([clef, dico_chaque_sommet[clef]])
            les_valeurs_rangees = []
            for couple in les_valeurs :
                if not les_valeurs_rangees : 
                    les_valeurs_rangees.append(couple)
                else :
                    if len(couple[1]) < len(les_valeurs_rangees[0][1]) :
                        les_valeurs_rangees.insert(0, couple)
            

            g.nodes[les_valeurs_rangees[0][0]]["Color"] = list(les_valeurs_rangees[0][1])[0]

"""