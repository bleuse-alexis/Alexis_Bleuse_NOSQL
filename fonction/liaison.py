from py2neo import Relationship

def liaison(df,useless,titre,genre,graph):

    df = df.drop(useless, axis=1)
    df = df.drop_duplicates().reset_index(drop=True)

    y = 0
    for c in df.columns:
        for i in df.index:
            if df[c][i] == 1:
                liaison = Relationship(titre[i], "type", genre[y])
                graph.merge(liaison)
        y = y + 1