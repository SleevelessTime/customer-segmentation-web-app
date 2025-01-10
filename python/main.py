import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

plt.style.use("ggplot")

_analysis_done = False

def perform_analysis_once():
    """Analizi sadece bir kez yapar, static/images içine grafik üretir."""
    global _analysis_done
    if _analysis_done:
        return

    # CSV dosyalarının bulunduğu klasör, bu "main.py" dosyasının olduğu yer
    BASE_DIR = os.path.dirname(__file__)

    train_path = os.path.join(BASE_DIR, "Train.csv")
    test_path = os.path.join(BASE_DIR, "Test.csv")
    sub_path = os.path.join(BASE_DIR, "sample_submission.csv")

    # Kaydedilecek klasör: static/images
    images_dir = os.path.join(os.path.dirname(BASE_DIR), "static", "images")
    # Not: os.path.dirname(BASE_DIR) => bir yukarı dizin, yani proje kökü
    # Orada "static/images" var. Gerekirse path'i düzenleyebilirsiniz.

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # 0) Veri Yükleme
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)
    df_sub = pd.read_csv(sub_path)

    print("Train shape:", df_train.shape)
    print("Test shape:", df_test.shape)
    print("Submission shape:", df_sub.shape)

    # 1) Eksik Değer
    num_cols = ["Age", "Work_Experience", "Family_Size"]
    cat_cols = ["Gender", "Ever_Married", "Graduated", "Profession", "Spending_Score", "Var_1"]

    for col in num_cols:
        df_train[col] = df_train[col].fillna(df_train[col].mean())
        df_test[col]  = df_test[col].fillna(df_test[col].mean())
    for col in cat_cols:
        df_train[col] = df_train[col].fillna(df_train[col].mode()[0])
        df_test[col]  = df_test[col].fillna(df_test[col].mode()[0])

    # 2) EDA Grafikleri
    plt.figure(figsize=(6, 4))
    sns.countplot(x="Segmentation", data=df_train, palette="Set2")
    plt.title("Train Setinde Segmentation Dağılımı")
    plt.xlabel("Segment (A,B,C,D)")
    plt.ylabel("Adet")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Train Setinde Segmentation Dağılımı.png"))
    plt.close()

    plt.figure(figsize=(6, 4))
    sns.countplot(x="Gender", data=df_train, palette="Set3")
    plt.title("Cinsiyet Dağılımı (Train)")
    plt.xlabel("Gender")
    plt.ylabel("Adet")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Cinsiyet Dağılımı.png"))
    plt.close()

    corr = df_train[num_cols].corr()
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
    plt.title("Sayısal Değişkenlerin Korelasyon Matrisi")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Sayısal Değişkenlerin Korelasyon Matrisi.png"))
    plt.close()

    plt.figure(figsize=(10, 5))
    sns.countplot(data=df_train, x="Profession", hue="Segmentation")
    plt.title("Profession dağılımı")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Profession dağılımı.png"))
    plt.close()

    # 3) Label Encoding
    le_cat = LabelEncoder()
    for col in cat_cols:
        df_train[col] = le_cat.fit_transform(df_train[col].astype(str))
        df_test[col]  = le_cat.transform(df_test[col].astype(str))

    le_seg = LabelEncoder()
    df_train["Segmentation"] = le_seg.fit_transform(df_train["Segmentation"].astype(str))
    y = df_train["Segmentation"].values

    X = df_train.drop(["ID", "Segmentation"], axis=1)
    test_ids = df_test["ID"].values
    X_test   = df_test.drop(["ID"], axis=1)

    # 4) Ölçekleme
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])
    X_test[num_cols] = scaler.transform(X_test[num_cols])

    # 5) Train-Val Split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6) Model Eğitimi
    params = {
        "n_estimators": [100, 200],
        "max_depth": [None, 10, 20]
    }
    rf_model = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(rf_model, param_grid=params, cv=3, scoring="f1_macro", n_jobs=-1)
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_
    print("Best Params:", grid.best_params_)

    y_val_pred = best_model.predict(X_val)
    print("\nVal Scores:\n", classification_report(y_val, y_val_pred))

    # 7) Confusion Matrix
    cf_matrix = confusion_matrix(y_val, y_val_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cf_matrix, annot=True, cmap="Reds", fmt="d")
    plt.title("Confusion Matrix (Validation)")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Confusion Matrix.png"))
    plt.close()

    # 8) Feature Importances
    feat_importances = best_model.feature_importances_
    features = X.columns
    imp_df = pd.DataFrame({"Feature": features, "Importance": feat_importances})
    imp_df.sort_values(by="Importance", ascending=False, inplace=True)

    plt.figure(figsize=(8, 5))
    sns.barplot(data=imp_df, x="Importance", y="Feature", palette="viridis")
    plt.title("Özellik Önem Sıralaması")
    plt.tight_layout()
    plt.savefig(os.path.join(images_dir, "Özellik Önem Sıralaması.png"))
    plt.close()

    # 9) Test setine uygulayıp submission
    final_preds = best_model.predict(X_test)
    final_labels = le_seg.inverse_transform(final_preds)

    submission_df = pd.DataFrame({"ID": test_ids, "Segmentation": final_labels})
    submission_path = os.path.join(os.path.dirname(BASE_DIR), "my_submission.csv")
    submission_df.to_csv(submission_path, index=False)

    print("\nSubmission saved. Head of submission:")
    print(submission_df.head(10))

    _analysis_done = True


IMAGE_MAPPING = {
    "scatter-4-values":        "Train Setinde Segmentation Dağılımı.png",
    "scatter-2-values":        "Cinsiyet Dağılımı.png",
    "confusion-matrix":        "Confusion Matrix.png",
    "feature-importance":      "Özellik Önem Sıralaması.png",
    "correlation-matrix":      "Sayısal Değişkenlerin Korelasyon Matrisi.png",
    "profession-distribution": "Profession dağılımı.png"
}

def run_analysis(graph_type):
    """
    Flask üzerinden, /show_graph?graph_type=... isteğine yanıt.
    1) Zaten startta perform_analysis_once() yapılmış olabilir, ama bir daha çağırsak da problem yok.
    2) graph_type'a göre 'static/images/...' yolunu döndürür.
    """
    perform_analysis_once()  # Tekrar etse bile _analysis_done ile korumalı

    if graph_type in IMAGE_MAPPING:
        return os.path.join("static", "images", IMAGE_MAPPING[graph_type])
    else:
        return ""
