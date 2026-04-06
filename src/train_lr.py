import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

from data_loader import load_data
from preprocess import clean_data
from feature_engineering import create_features

FEATURES = [
    "CIF",
    "FOB",
    "AJUSTE",
    "CODIGO_ADUANA",
    "YEAR",
    "FOB_CIF_RATIO"
]

# 1. cargar data
df = load_data("data/raw/import_data.csv")
df.columns = df.columns.str.strip()

# 2. limpiar
df = clean_data(df)

# 3. features
df = create_features(df)

# 4. target
y = df["INSPECCION"]

le = LabelEncoder()
y = le.fit_transform(y)

# 5. X
X = df[FEATURES]

# 6. split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# modelo
model = LogisticRegression(
    class_weight="balanced",
    max_iter=1000
)

model.fit(X_train, y_train)

# guardar
joblib.dump(model, "models/model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("✅ Logistic Regression entrenado")