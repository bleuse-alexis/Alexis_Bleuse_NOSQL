from py2neo import Node

def film(df,graph,useless,var):

    df = df.drop(useless, axis=1)
    Titre = []
    df=df.drop_duplicates()
    for c in df[var]:
        titre=Node(var,name=c)
        Titre.append(titre)
        graph.create(titre)
    return Titre

def genre(df,graph,useless,var):

    df=df.drop(useless, axis=1)
    Genre=[]
    df=df.drop_duplicates()
    for c in df.columns:
        genre=Node(var,name=c)
        Genre.append(genre)
        graph.create(genre)
    return Genre
