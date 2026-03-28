import pandas as pd

# Sample dataset
data = {"Name":["Alice","Bob","Charlie"],"Score":[85,72,90]}
df = pd.DataFrame(data)

print(df.head())              # top rows
print(df.max())               # highest value column
print(df.isna().sum())        # missing values

