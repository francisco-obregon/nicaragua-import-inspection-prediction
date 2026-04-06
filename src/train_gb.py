import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

from data_loader import load_data
from preprocess import clean_data
from feature_engineering import create_features

# features 
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

# limpiar columnas
df.columns = df.columns.str.strip()

# 2. limpiar data
df = clean_data(df)

# 3. feature engineering
df = create_features(df)

# 4. target 
y = df["INSPECCION"]

# usar LabelEncoder 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# 5. features
X = df[FEATURES]

# 6. split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. modelo Gradient Boosting
model = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# 8. guardar modelo y encoder
joblib.dump(model, "models/model.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("✅ Modelo Gradient Boosting entrenado y guardado")