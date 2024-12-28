import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyalarını yükleme
train = pd.read_csv("Train.csv")
test = pd.read_csv("Test.csv")

# Eksik değerlerin sütun bazında toplamı
missing_train = train.isnull().sum()
missing_test = test.isnull().sum()

# Eksik değerlerin sadece eksik veri içeren sütunlarını filtreleme
missing_train = missing_train[missing_train > 0]
missing_test = missing_test[missing_test > 0]

# Eksik değerleri görselleştirme
plt.figure(figsize=(10, 6))
plt.bar(missing_train.index, missing_train.values, label="Train", alpha=0.7, color="blue")
plt.bar(missing_test.index, missing_test.values, label="Test", alpha=0.7, color="orange")
plt.xlabel("Sütunlar")
plt.ylabel("Eksik Değer Sayısı")
plt.title("Eksik Değerlerin Dağılımı")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Görseli kaydetme
plt.savefig("missing_values_distribution.png")
plt.show()
