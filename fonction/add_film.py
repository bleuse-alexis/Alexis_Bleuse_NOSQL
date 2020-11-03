from py2neo import Node, Relationship, Graph

def film(df,graph):
    gen=['Musical','Animation','Action','Children','Adventure','Western','(no genres listed)','Thriller','War','Crime','Horror','Drama','Film-Noir','Romance','Sci-Fi','Comedy','Fantasy','Mystery','Documentary']
    df=df.drop(gen, axis=1)

    useless = ['index', 'movieId', 'year', 'IMAX', 'userId_x', 'rating', 'timestamp_x', 'ratings_nb', 'userId_y', 'tag','timestamp_y']
    df = df.drop(useless, axis=1)

    df=df.drop_duplicates()
    for c in df['title']:
        titre=Node('title',name=c)
        graph.create(titre)


def genre(df,graph):
    gen=['Musical','Animation','Action','Children','Adventure','Western','(no genres listed)','Thriller','War','Crime','Horror','Drama','Film-Noir','Romance','Sci-Fi','Comedy','Fantasy','Mystery','Documentary']
    df['Genre']= df[gen].idxmax(1)
    df=df.drop(gen, axis=1)

    useless=['index','movieId','year','IMAX','userId_x','rating','timestamp_x','ratings_nb','userId_y','tag','timestamp_y','title']
    df=df.drop(useless, axis=1)

    df=df.drop_duplicates()
    for c in df['Genre']:
        genre=Node('genre',name=c)
        graph.create(genre)
