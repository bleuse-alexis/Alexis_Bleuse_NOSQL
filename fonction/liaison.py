from py2neo import Relationship

def creation_liaison(df,useless,titre,genre,graph):

    '''
    :param df: le dataframe sur lequel appliquer la fonction
    :param useless: la liste des colonnes à supprimer
    :param titre: la liste des film en node
    :param genre: la liste des genre en node
    :param graph: la variable qui va permettre d'envoyer les relationships
    '''

    df = df.drop(useless, axis=1)
    df = df.drop_duplicates().reset_index(drop=True)

    y = 0
    for c in df.columns:
        for i in df.index:
            if df[c][i] == 1:
                liaison = Relationship(titre[i], "type", genre[y])
                graph.create(liaison)
        y = y + 1