import sqlite3
import pandas as pd

# conectar a la base de datos
conn = sqlite3.connect("data/imports.db")

# Query 1: promedio de impuestos por año
query1 = """
SELECT YEAR, AVG(PAGADO) as avg_pagado
FROM imports
GROUP BY YEAR;
"""

df1 = pd.read_sql(query1, conn)
print("\n📊 Promedio de impuestos por año:")
print(df1)


# Query 2: cantidad de inspecciones
query2 = """
SELECT INSPECCION, COUNT(*) as total
FROM imports
GROUP BY INSPECCION;
"""

df2 = pd.read_sql(query2, conn)
print("\n📊 Cantidad de inspecciones:")
print(df2)


# Query 3: top aduanas con más inspecciones
query3 = """
SELECT CODIGO_ADUANA, COUNT(*) as total
FROM imports
WHERE INSPECCION = 'INSPECCION'
GROUP BY CODIGO_ADUANA
ORDER BY total DESC;
"""

df3 = pd.read_sql(query3, conn)
print("\n📊 Top aduanas con más inspecciones:")
print(df3)

# guardar resultados
df1.to_csv("data/processed/avg_pagado_by_year.csv", index=False)
df2.to_csv("data/processed/inspections_distribution.csv", index=False)
df3.to_csv("data/processed/top_customs.csv", index=False)


# cerrar conexión
conn.close()