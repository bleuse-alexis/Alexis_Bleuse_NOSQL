import pandas as pd
from fonction.add_film import film_node, genre_node
from fonction.liaison import creation_liaison
from py2neo import Graph

pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_json("movies_rated_tagged.json")

useless = ['index', 'movieId', 'year', 'IMAX', 'userId_x', 'rating', 'timestamp_x', 'ratings_nb',
           'userId_y', 'tag','timestamp_y', 'title']

uselessf = ['index', 'movieId', 'year', 'IMAX', 'userId_x', 'rating', 'timestamp_x', 'ratings_nb',
            'userId_y', 'tag','timestamp_y','Musical','Animation','Action','Children','Adventure',
            'Western','(no genres listed)','Thriller','War','Crime','Horror','Drama','Film-Noir',
            'Romance','Sci-Fi','Comedy','Fantasy','Mystery','Documentary']

varf='title'
varg='genre'

graph = Graph()
graph.delete_all()

titre=film_node(df,graph,uselessf,varf)
genre=genre_node(df,graph,useless,varg)
creation_liaison(df,useless,titre,genre,graph)