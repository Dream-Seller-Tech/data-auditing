import pandas as pd

df = pd.read_csv('KaggleV2-May-2016')
print(df)




duplicates = df[df.duplicated(keep=False)]

duplicate_rows = duplicates.index

print("Duplicate rows:", duplicate_rows)
