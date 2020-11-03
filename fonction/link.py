from py2neo import Node, Relationship, Graph, NodeMatcher

def creation_dico(df):
    useless = ['index','movieId', 'year', 'IMAX', 'userId_x', 'rating', 'timestamp_x', 'ratings_nb', 'userId_y', 'tag','timestamp_y']
    df = df.drop(useless, axis=1)
    gen=['Musical','Animation','Action','Children','Adventure','Western','(no genres listed)','Thriller','War','Crime','Horror','Drama','Film-Noir','Romance','Sci-Fi','Comedy','Fantasy','Mystery','Documentary']
    df['Genre']= df[gen].idxmax(1)
    df=df.drop(gen, axis=1)

    df=df.drop_duplicates()
    dico={}
    for i in df.index:
        dico[Node('titre',name=df['title'][i])]=[Node('genre',name=df['Genre'][i])]

    return dico


def link(graph,dico):
    matcher = NodeMatcher(graph)
    for key,value in dico.items():
        if len(matcher.match("titre").where(name=key)) == 0:
            liaison = Relationship(key, "type", value)
        else:
            liaison = graph.merge_one(key,"type",value)
        graph.create(liaison)

