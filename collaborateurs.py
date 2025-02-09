# import json
# import matplotlib.pyplot as plt
# import networkx as nx

# # Question 6.1
# def enlever_elem(nom):
#     """Fonction enlevant les éléments indésirable dans les noms des acteurs
    
#     Parametres:
#         nom: nom de l'acteur
#     """
#     elem = "[']"
#     for x in range(len(elem)):
#         nom = nom.replace(elem[x],"")
#     v = nom.split("|")
#     nom = v[-1]
#     return nom


# def convertisseur(fichier):
#     """Fonction renvoyant le Graph à partir d'un fichier texte

#     Parametres:
#         fichier : un fichier .txt
#     """
#     G = nx.Graph() # Création du graph
#     fic = open(fichier,'r',encoding = "utf-8") # Lecture du fichier text
#     for lignes in fic: # Parcour du fichier par ligne
#         dico = json.loads(lignes) # Initialisation automatique du dictionnaire à partir des données du fichier pour chaque film
#         for i in range (len(dico["cast"])): # Parcours du dictionnaire des acteurs 
#             dico["cast"][i] = enlever_elem(dico["cast"][i]) # Remplace le nom des acteurs et les remets au propre
#             if dico["cast"][i] not in G: # S'il n'est pas déjà dans le Graph, le mettre
#                 G.add_node(dico["cast"][i],label='A')
        
#         for acteur1 in dico["cast"]: # Pour chaque acteur former un lien entre eux dans le Graph pour signifier qu'ils ont travaillé ensemble 
#             for acteur2 in dico["cast"]:
#                 if (acteur1,acteur2) not in G and acteur1 != acteur2:
#                     G.add_edge(acteur1,acteur2)
    
#     nx.draw(G,with_labels = True) # Dessiner puis afficher graph
#     plt.show()
#     return G 

# print(convertisseur("données/data_100.txt"))

# # Question 6.2
# def collab_commun(acteur1, acteur2,fichier):
#     """Fonction renvoyant l'ensemble des acteurs ayant collaboré avec ces 2 acteurs placé en parametre'

#     Parametres:
#         acteur1 : un acteur
#         acteur2 : un acteur
#         fichier : un fichier .txt
#     """
#     collab = set() # Initialisation de l'ensemble des collaborateurs
#     G = convertisseur(fichier) # Appel de la fonction convertisseur pour reprendre le Graph
#     for acteur in G.nodes: # Pour chaque acteur du graph s'il n'est pas égal aux 2 acteurs et qu'il a déjà travaillé avec ces 2 acteurs, on l'ajouterai à l'ensemble
#         if acteur != acteur1 and acteur != acteur2:
#             if (acteur1,acteur) in G.edges and (acteur2,acteur) in G.edges:
#                 collab.add(acteur)
#     return collab

# # Question 6.3
# # Fonction donnée
# def collaborateurs_proches(G,u,k):
#     """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
#     Parametres:
#         G: le graphe
#         u: le sommet de départ
#         k: la distance depuis u
#     """
#     if u not in G.nodes:
#         print(u,"est un illustre inconnu")
#         return None
#     collaborateurs = set()
#     collaborateurs.add(u)
#     print(collaborateurs)
#     for i in range(k):
#         collaborateurs_directs = set()
#         for c in collaborateurs:
#             for voisin in G.adj[c]:
#                 if voisin not in collaborateurs:
#                     collaborateurs_directs.add(voisin)
#         collaborateurs = collaborateurs.union(collaborateurs_directs)
#     return collaborateurs

# def collaborateurs_proches(acteur_dep,acteur_fin,fichier):
#     """Fonction renvoyant la distance entre 2 acteurs.
    
#     Parametres:
#         acteur_dep : le sommet de départ
#         acteur_fin : le somemt de fin
#         fichier : un fichier .txt
#     """
#     G = convertisseur(fichier) # Appel de la fonction convertisseur pour reprendre le Graph
#     if acteur_dep not in G.nodes: # Si l'acteur placé en parametre n'est pas dans le graph return None
#         print(acteur_dep,"est un illustre inconnu")
#         return None
#     collaborateurs = set() # Initialisation de l'ensemble des collaborateurs 
#     collaborateurs.add(acteur_dep) # On ajoute dans l'ensemble l'acteur de départ
#     count = 0 # Inialisation d'un compteur pour calculer la distance entre ces 2 acteurs
#     while acteur_fin not in collaborateurs: # Tant que l'acteur de fin n'est pas dans l'ensemble des collaborateurs, parcourir en largeur le graph
#         test = False # Initialisation d'un testeur d'action pour vérifier que nous ne sommes pas dans une boucle infini
#         collaborateurs_directs = set() # Inialisationd d'un nouvel ensemble des collaborateurs direct pour chaque tour de boucle
#         for c in collaborateurs: # Parcours de chaque collaborateurs
#             for voisin in G.adj[c]: # Parcours de tout les voisins des collaborateurs 
#                 if voisin not in collaborateurs: # On ajoute ces voisins à l'ensemble des collaborateurs s'ils ne sont pas déjà dedans et on ajoute 1 au compteur
#                     collaborateurs_directs.add(voisin)
#                     test = True
#         count +=1
#         collaborateurs = collaborateurs.union(collaborateurs_directs)
#         if test == False :
#             print (acteur_dep, " et ", acteur_fin," n'ont aucune connexions.")
#             return None

#     return count

# #Question 6.4
# def central(acteur,fichier):
#     """Fonction renvoyant la valeur de centralité d'un acteur

#     Parametres:
#         acteur : nom de l'acteur dont on veut la centralité
#         fichier : un fichier .txt
#     """
#     G = convertisseur(fichier) # Appel de la fonction convertisseur pour reprendre le graph
#     dico = nx.centrality.betweenness.betweenness_centrality(G) # Initialisation d'un dictionnaire de la centralisation de chaque acteur
#     for nom, value in dico.items():
#         if acteur == nom:
#             return value
#     return 0



# def pluscentral(fichier):
#     """Fonction renvoyant l'acteur a la plus haute centralité

#     Parametres:
#         fichier : un fichier .txt
#     """
#     G = convertisseur(fichier) # Appel de la fonction convertisseur pour reprendre le Graph
#     valmax=0 # l'acteur avec la valeur max de centralité
#     actmax=""
#     for acteur in G.nodes: # Boucle for cherchant la valeur max de centralité et renvoyant l'acteur avec la plus haute valeur de centralité
#         if central(acteur,fichier) > valmax:
#             valmax=central(acteur,fichier)
#             actmax=acteur
#     return actmax

# # Question 6.5
# def pluseloigne(fichier):
#     """Fonction renvoyant le couple d'acteur/actrice le plus éloigné
#     Parametres:
#         fichier : un fichier .txt
#     """
#     G = convertisseur(fichier) # Appel de la fonction convertisseur pour reprendre le Graph
#     distmax = 0 # La distance qui sera la plus éloigné et leurs acteurs
#     actmax=("","")
#     for (acteur1,acteur2) in G.edges: # Parcours de toutes les arrètes du graph
#         if collaborateurs_proches(acteur1,acteur2,fichier)>distmax:
#             distmax=collaborateurs_proches(acteur1,acteur2,fichier)
#             actmax=(acteur1,acteur2)
#     return actmax


import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def enlever_elem(nom):
    """Fonction enlevant les éléments indésirables dans les noms des acteurs"""
    elem = "[]'"
    for x in elem:
        nom = nom.replace(x, "")
    nom = nom.split("|")[-1]
    return nom

def convertisseur(fichier):
    """Fonction renvoyant le Graph à partir d'un fichier texte"""
    G = nx.Graph()
    with open(fichier, 'r', encoding="utf-8") as fic:
        for lignes in fic:
            dico = json.loads(lignes)
            for i in range(len(dico["cast"])):
                dico["cast"][i] = enlever_elem(dico["cast"][i])
                if dico["cast"][i] not in G:
                    G.add_node(dico["cast"][i], label='A')
            
            for acteur1 in dico["cast"]:
                for acteur2 in dico["cast"]:
                    if acteur1 != acteur2:
                        G.add_edge(acteur1, acteur2)
    
    nx.draw(G, with_labels=True)
    plt.show()
    return G

def collab_commun(acteur1, acteur2, fichier):
    """Fonction renvoyant l'ensemble des acteurs ayant collaboré avec ces 2 acteurs"""
    G = convertisseur(fichier)
    collab = {acteur for acteur in G.nodes if acteur != acteur1 and acteur != acteur2 and 
              (acteur1, acteur) in G.edges and (acteur2, acteur) in G.edges}
    return collab

def collaborateurs_proches(G, u, k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G"""
    if u not in G:
        print(u, "est un illustre inconnu")
        return None
    collaborateurs = {u}
    for _ in range(k):
        collaborateurs.update(voisin for c in collaborateurs for voisin in G[c] if voisin not in collaborateurs)
    return collaborateurs

def distance_acteurs(acteur_dep, acteur_fin, fichier):
    """Fonction renvoyant la distance entre 2 acteurs."""
    G = convertisseur(fichier)
    if acteur_dep not in G:
        print(acteur_dep, "est un illustre inconnu")
        return None
    try:
        return nx.shortest_path_length(G, source=acteur_dep, target=acteur_fin)
    except nx.NetworkXNoPath:
        print(acteur_dep, "et", acteur_fin, "n'ont aucune connexion.")
        return None

def central(acteur, fichier):
    """Fonction renvoyant la valeur de centralité d'un acteur"""
    G = convertisseur(fichier)
    centrality = nx.betweenness_centrality(G)
    return centrality.get(acteur, 0)

def pluscentral(fichier):
    """Fonction renvoyant l'acteur avec la plus haute centralité"""
    G = convertisseur(fichier)
    centrality = nx.betweenness_centrality(G)
    return max(centrality, key=centrality.get)

def pluseloigne(fichier):
    """Fonction renvoyant le couple d'acteurs/actrices le plus éloigné"""
    G = convertisseur(fichier)
    return max(nx.all_pairs_shortest_path_length(G), key=lambda x: x[1].get(max(x[1], key=x[1].get)))

if __name__ == "__main__":
    fichier = "données/data_100.txt"
    
    # Exemples d'appels aux fonctions
    print("Création et affichage du graphe")
    G = convertisseur(fichier)

    acteur1 = "Acteur A"
    acteur2 = "Acteur B"
    
    print(f"Collaborateurs communs entre {acteur1} et {acteur2} :")
    print(collab_commun(acteur1, acteur2, fichier))

    acteur_dep = "Acteur A"
    acteur_fin = "Acteur B"
    
    print(f"Distance entre {acteur_dep} et {acteur_fin} :")
    print(distance_acteurs(acteur_dep, acteur_fin, fichier))

    acteur = "Acteur A"
    
    print(f"Centralité de {acteur} :")
    print(central(acteur, fichier))
    
    print("Acteur avec la plus haute centralité :")
    print(pluscentral(fichier))

    print("Couple d'acteurs le plus éloigné :")
    print(pluseloigne(fichier))


class GraphML(object):
    (int, "int"), (np.int8, "int"),
