import joblib

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from data_loader import load_data
from preprocess import clean_data
from feature_engineering import create_features

# 1. cargar modelo
model = joblib.load("models/model.pkl")

# 2. cargar data
df = load_data("data/raw/import_data.csv")

# limpiar nombres
df.columns = df.columns.str.strip()

# 3. preprocess
df = clean_data(df)

# 4. features
df = create_features(df)

# 5. target
y = df["INSPECCION"]

le = joblib.load("models/label_encoder.pkl")
y = le.transform(y)

# 6. features
FEATURES = [
    "CIF",
    "FOB",
    "AJUSTE",
    "CODIGO_ADUANA",
    "YEAR",
    "FOB_CIF_RATIO"
]

X = df[FEATURES]

# 7. split (igual que train)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 8. predicción
y_pred = model.predict(X_test)

# 9. métricas
print("\n📊 CLASSIFICATION REPORT:")
print(classification_report(y_test, y_pred))

print("\n🧱 CONFUSION MATRIX:")
print(confusion_matrix(y_test, y_pred))

print("\n🎯 Accuracy:", accuracy_score(y_test, y_pred))
print("\nClases:", le.classes_)