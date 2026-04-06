import pandas as pd

df = pd.read_csv("data/raw/import_data.csv", encoding="latin-1", sep=";")

print("\nHEAD:")
print(df.head())

print("\nINFO:")
print(df.info())

print("\nNULLS:")
print(df.isnull().sum())

print("\nDUPLICATES:")
print(df.duplicated().sum())

print("\nPAGADO STATS:")
print(df["PAGADO"].describe())