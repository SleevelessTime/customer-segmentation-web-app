##################################################
# Kaggle'dan alınan Müşteri Segmentasyonu verisi:
# "VERİ MADENCİLİĞİ" dersi projesi için
# EDA + Model + Görseller
##################################################

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

plt.style.use("ggplot")  # Plotları daha güzel göstermek için

def main():
    ##################################################
    # 0) Veri Yükleme
    ##################################################
    df_train = pd.read_csv("Train.csv")
    df_test  = pd.read_csv("Test.csv")
    df_sub   = pd.read_csv("sample_submission.csv")

    print("Train shape:", df_train.shape)
    print("Test shape:", df_test.shape)
    print("Submission shape:", df_sub.shape)

    print("\n--- TRAIN HEAD ---")
    print(df_train.head())

    print("\n--- TEST HEAD ---")
    print(df_test.head())

    ##################################################
    # 1) Eksik Değer Analizi
    ##################################################
    print("\n--- Null Check (Train) ---")
    print(df_train.isnull().sum())

    print("\n--- Null Check (Test) ---")
    print(df_test.isnull().sum())

    # Numerik ve kategorik sütunlar
    num_cols = ["Age", "Work_Experience", "Family_Size"]
    cat_cols = ["Gender", "Ever_Married", "Graduated",
                "Profession", "Spending_Score", "Var_1"]

    # Eksikleri dolduralım
    for col in num_cols:
        df_train[col] = df_train[col].fillna(df_train[col].mean())
        df_test[col]  = df_test[col].fillna(df_test[col].mean())

    for col in cat_cols:
        df_train[col] = df_train[col].fillna(df_train[col].mode()[0])
        df_test[col]  = df_test[col].fillna(df_test[col].mode()[0])

    ##################################################
    # 2) EDA (Grafikler)
    ##################################################

    # 2.1 Segmentation dağılımı (Train'de)
    plt.figure(figsize=(6,4))
    sns.countplot(x="Segmentation", data=df_train, hue=None, palette="Set2")
    plt.title("Train Setinde Segmentation Dağılımı")
    plt.xlabel("Segment (A,B,C,D)")
    plt.ylabel("Adet")
    plt.show()

    # 2.2 Gender dağılımı (Train'de)
    plt.figure(figsize=(6,4))
    sns.countplot(x="Gender", data=df_train, hue=None, palette="Set3")
    plt.title("Cinsiyet Dağılımı (Train)")
    plt.xlabel("Gender")
    plt.ylabel("Adet")
    plt.show()

    # 2.3 Korelasyon Matrisi (Sayısal değişkenler)
    corr = df_train[num_cols].corr()
    plt.figure(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f")
    plt.title("Sayısal Değişkenlerin Korelasyon Matrisi")
    plt.show()

    # 2.4 Profession vs Segmentation (countplot)
    plt.figure(figsize=(10,5))
    sns.countplot(data=df_train, x="Profession", hue="Segmentation")
    plt.title("Profession dağılımı, Segmentation'a göre")
    plt.xticks(rotation=45)
    plt.show()


    ##################################################
    # 3) Label Encoding + Feature Hazırlığı
    ##################################################

    le_cat = LabelEncoder()
    for col in cat_cols:
        df_train[col] = le_cat.fit_transform(df_train[col].astype(str))
        df_test[col]  = le_cat.transform(df_test[col].astype(str))

    # Segmentation'ı encode
    le_seg = LabelEncoder()
    df_train["Segmentation"] = le_seg.fit_transform(df_train["Segmentation"].astype(str))
    y = df_train["Segmentation"].values

    # X oluştur
    X = df_train.drop(["ID","Segmentation"], axis=1)
    test_ids = df_test["ID"].values
    X_test   = df_test.drop(["ID"], axis=1)

    ##################################################
    # 4) Ölçekleme
    ##################################################
    scaler = StandardScaler()
    X[num_cols] = scaler.fit_transform(X[num_cols])
    X_test[num_cols] = scaler.transform(X_test[num_cols])

    ##################################################
    # 5) Train-Val Split
    ##################################################
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    ##################################################
    # 6) Model Eğitimi (RandomForest) + GridSearch
    ##################################################
    params = {
        "n_estimators": [100, 200],
        "max_depth": [None, 10, 20]
    }

    rf_model = RandomForestClassifier(random_state=42)
    grid = GridSearchCV(
        rf_model,
        param_grid=params,
        cv=3,
        scoring="f1_macro",
        n_jobs=-1
    )
    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_

    y_val_pred = best_model.predict(X_val)
    print("Best Params:", grid.best_params_)

    print("\nVal Scores after GridSearch:")
    print(classification_report(y_val, y_val_pred))

    ##################################################
    # 7) Confusion Matrix (Val)
    ##################################################
    cf_matrix = confusion_matrix(y_val, y_val_pred)
    print("Confusion Matrix (Val):\n", cf_matrix)

    plt.figure(figsize=(5,4))
    sns.heatmap(cf_matrix, annot=True, cmap="Reds", fmt="d")
    plt.title("Confusion Matrix (Validation Set)")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()

    ##################################################
    # 8) Feature Importance Grafiği
    ##################################################
    feat_importances = best_model.feature_importances_
    features = X.columns
    imp_df = pd.DataFrame({
        "Feature": features,
        "Importance": feat_importances
    }).sort_values(by="Importance", ascending=False)

    plt.figure(figsize=(8,5))
    sns.barplot(data=imp_df, x="Importance", y="Feature", hue=None, palette="viridis")
    plt.title("Özellik Önem Sıralaması (RandomForest)")
    plt.tight_layout()
    plt.show()

    ##################################################
    # 9) Test setine uygulayıp Submission kaydetme
    ##################################################
    final_preds = best_model.predict(X_test)  # numeric 0,1,2,3
    final_labels = le_seg.inverse_transform(final_preds)  # geri A,B,C,D haline

    submission_df = pd.DataFrame({
        "ID": test_ids,
        "Segmentation": final_labels
    })
    submission_df.to_csv("my_submission.csv", index=False)

    print("\nSubmission saved. Head of submission:")
    print(submission_df.head(10))


if __name__ == "__main__":
    main()
