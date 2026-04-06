import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="latin-1", sep=";", engine="python")
    return df