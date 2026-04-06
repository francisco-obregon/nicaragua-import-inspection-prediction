import pandas as pd
import matplotlib.pyplot as plt

# cargar data
df = pd.read_csv("data/raw/import_data.csv", encoding="latin-1", sep=";")

# limpiar columnas
df.columns = df.columns.str.strip()

# 1. % INSPECCIONES (BAR)

inspection_counts = df["INSPECCION"].value_counts(normalize=True) * 100

plt.figure()
inspection_counts.plot(kind="bar")
plt.title("Inspection Percentage (%)")
plt.ylabel("Percentage")
plt.xticks(rotation=0)

plt.savefig("visuals/inspection_percentage.png")


# 2. FRECUENCIA POR ADUANA (LINE)

# contar inspecciones por aduana
customs_counts = (
    df[df["INSPECCION"] == "INSPECCION"]
    .groupby("CODIGO_ADUANA")
    .size()
    .sort_index()
)

# ordenar por código de aduana
plt.figure(figsize=(10,5))

customs_counts.plot(kind="bar")

plt.title("Inspection Frequency by Customs Office")
plt.xlabel("Customs Code")
plt.ylabel("Number of Inspections")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visuals/inspection_by_customs.png")

print("✅ Visuals generados correctamente")