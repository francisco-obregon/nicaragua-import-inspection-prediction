import joblib
import pandas as pd

from preprocess import clean_data
from feature_engineering import create_features


# 1. cargar modelo y encoder
model = joblib.load("models/model.pkl")
le = joblib.load("models/label_encoder.pkl")


def predict_file(input_path, output_path):
    # 2. cargar data
    df = pd.read_csv(input_path, encoding="latin-1", sep=";")

    # limpiar columnas
    df.columns = df.columns.str.strip()

    # 3. preprocess
    df = clean_data(df)

    # 4. feature engineering
    df = create_features(df)

    # 5. features
    FEATURES = [
    "CIF",
    "FOB",
    "AJUSTE",
    "CODIGO_ADUANA",
    "YEAR",
    "FOB_CIF_RATIO"
    ]

    X = df[FEATURES]

    # 6. predicciones
    preds = model.predict(X)

    # 7. convertir a texto
    df["PREDICCION"] = le.inverse_transform(preds)

    # 8. guardar resultado
    df.to_excel(output_path, index=False)

    print(f"✅ Archivo guardado en {output_path}")
    

# ejecutar
if __name__ == "__main__":
    predict_file(
        "data/raw/import_data.csv",
        "data/processed/predictions.xlsx"
    )