from sklearn.preprocessing import StandardScaler
import pandas as pd

# CSV dosyanızı yükleyin
train_path = "Train.csv"  # Kendi dosyanızın yolunu buraya yazın
df = pd.read_csv(train_path)

# Kontrol etmek istediğiniz sütunları seçin
columns_to_check = ["Age", "Work_Experience", "Family_Size"]  # Dönüşüm yapılacak sütunlar
selected_data = df[columns_to_check].dropna()  # Eksik değerleri çıkarın

# Ortalama ve standart sapma değerlerini hesaplayın
mean_values = selected_data.mean()
std_values = selected_data.std()

# StandardScaler ile ölçeklendirme
scaler = StandardScaler()
scaled_values = scaler.fit_transform(selected_data)

# Sonuçları görselleştirin
scaled_df = pd.DataFrame(scaled_values, columns=columns_to_check)
print("Ortalama Değerler:\n", mean_values)
print("Standart Sapmalar:\n", std_values)
print("Ölçeklenmiş Değerler:\n", scaled_df.head())

# Spesifik bir örnek kontrolü
specific_example = pd.DataFrame([[45, 10, 4]], columns=columns_to_check)
scaled_example = scaler.transform(specific_example)
print("Özel Örnek Ölçeklenmiş Değerler:\n", scaled_example)
