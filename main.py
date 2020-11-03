import pandas as pd
from py2neo import Node, Relationship, Graph
from fonction.add_film import film, genre
from fonction.link import link,creation_dico


pd.set_option("display.max_rows", None, "display.max_columns", None);

df = pd.read_json("movies_rated_tagged.json")

graph = Graph()
graph.delete_all()

#film(df,graph)
#genre(df,graph)
dico=creation_dico(df)

#print(dico)
link(graph,dico)

