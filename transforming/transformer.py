import pandas as pd

df = pd.read_csv("output/internships.csv")
df.columns = ["title", "company", "location", "position", "skills"]
df = df.dropna()
for col in df.columns:
    df[col] = df[col].str.lower()
df = df.drop_duplicates()
df.to_csv('output/clean.csv', index=False)