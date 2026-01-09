import pandas as pd

df = pd.read_csv('liste_actions.csv', encoding="latin-1")
print(df.info())



print(df["Action"])