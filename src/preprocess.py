import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="latin-1", sep=";", engine="python")
    return df

def clean_data(df):
    # eliminar duplicados
    df = df.drop_duplicates()

    # manejar nulos
    df["COLOR_GENERAL"] = df["COLOR_GENERAL"].fillna("UNKNOWN")
    df["DSC_CONTRIBUYENTE"] = df["DSC_CONTRIBUYENTE"].fillna("UNKNOWN")

    return df