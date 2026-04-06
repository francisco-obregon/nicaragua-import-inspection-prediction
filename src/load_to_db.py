import pandas as pd
import sqlite3

# cargar CSV
df = pd.read_csv("data/raw/import_data.csv", encoding="latin-1", sep=";")

df.columns = df.columns.str.strip()

# conectar DB
conn = sqlite3.connect("data/imports.db")

# guardar como tabla
df.to_sql("imports", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data cargada en SQLite como tabla 'imports'")