import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None);

df = pd.read_json("movies_rated_tagged.json")

#print(df.head())

print(df['title'].value_counts(dropna=False).sort_index())
print(df['title'].value_counts(dropna=False).sum())
