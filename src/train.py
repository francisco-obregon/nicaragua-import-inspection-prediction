import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from data_loader import load_data
from preprocess import clean_data
from feature_engineering import create_features

# 1. cargar data
df = load_data("data/raw/import_data.csv")

df.columns = df.columns.str.strip()

# 2. limpiar data
df = clean_data(df)

# 3. feature engineering
df = create_features(df)

# 4. definir target
y = df["INSPECCION"]

# convertir target a números
le = LabelEncoder()
y = le.fit_transform(y)

# 5. seleccionar features
FEATURES = [
    "CIF",
    "FOB",
    "AJUSTE",
    "CODIGO_ADUANA",
    "YEAR",
    "FOB_CIF_RATIO"
]

X = df[FEATURES]

# 6. dividir data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. entrenar modelo
model = RandomForestClassifier(
    class_weight="balanced",
    n_estimators=100,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

# 8. guardar modelo
joblib.dump(model, "models/model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("Modelo y encoder guardados ✅")