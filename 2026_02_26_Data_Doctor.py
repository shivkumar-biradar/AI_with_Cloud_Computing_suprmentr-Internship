import pandas as pd

data = {"Name":["Alice","Bob","Alice"],"Score":[85,None,85]}
df = pd.DataFrame(data)

df = df.drop_duplicates()
df["Score"] = df["Score"].fillna(df["Score"].mean())
df["Name"] = df["Name"].str.title()

print(df)
