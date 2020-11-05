from py2neo import Node

def film_node(df,graph,useless,var):

    '''
    :param df: le dataframe sur lequel appliquer la fonction
    :param graph: la variable qui va permettre d'envoyer les nodes
    :param useless: la liste des colonnes à supprimer
    :param var: le nom de la colonne où creer les nodes
    :return: la liste des nodes créés
    '''

    df = df.drop(useless, axis=1)
    Titre = []
    df=df.drop_duplicates()
    for c in df[var]:
        titre=Node(var,name=c)
        Titre.append(titre)
        graph.create(titre)
    return Titre

def genre_node(df,graph,useless,var):

    '''
    :param df: le dataframe sur lequel appliquer la fonction
    :param graph: la variable qui va permettre d'envoyer les nodes
    :param useless: la liste des colonnes à supprimer
    :param var: le nom de la colonne où creer les nodes
    :return: la liste des nodes créés
    '''

    df=df.drop(useless, axis=1)
    Genre=[]
    df=df.drop_duplicates()
    for c in df.columns:
        genre=Node(var,name=c)
        Genre.append(genre)
        graph.create(genre)
    return Genre
