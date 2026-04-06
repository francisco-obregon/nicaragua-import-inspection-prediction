import numpy as np

def create_features(df):
    # relación válida
    df["FOB_CIF_RATIO"] = df["FOB"] / df["CIF"]

    return df