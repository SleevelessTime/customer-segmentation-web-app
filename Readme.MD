# Müşteri Segmentasyonu Projesi

Bu proje, İstanbul Arel Üniversitesi Veri Madenciliği dersi kapsamında hazırlanmıştır. Projenin amacı, müşteri segmentasyonunu gerçekleştirmek ve elde edilen sonuçları analiz etmektir.

---

## 📁 Proje Dosyaları
- `Train.csv`: Eğitim veri seti (8068 satır, 11 sütun)
- `Test.csv`: Test veri seti (2627 satır, 10 sütun)
- `my_submission.csv`: Test veri setindeki müşteri segment tahminlerini içerir.
- `missing_values_distribution.png`: Eksik değerlerin dağılımını gösteren grafik.
- `plot_*.png`: Proje kapsamında oluşturulan görseller (Toplam 6 adet).

---

## 📊 Kullanılan Adımlar ve Teknikler

### 1. **Eksik Değer Analizi**
Eksik değerlerin bulunduğu sütunlar:
- `Ever_Married`, `Graduated`, `Profession`, `Work_Experience`, `Family_Size`, `Var_1`

Eksik değer doldurma yöntemleri:
- **Numerik Sütunlar:** Ortalama (\textit{mean})
- **Kategorik Sütunlar:** Mod (\textit{mode})

Eksik değerlerin dağılımı görselleştirilmiş ve doldurma sonrası eksik değer bulunmamaktadır.

### 2. **Veri Dönüşümleri**
- **Label Encoding:** Kategorik sütunlar sayısal değerlere dönüştürülmüştür.
- **StandardScaler:** `Age`, `Work_Experience`, `Family_Size` değişkenleri ölçeklendirilmiştir.

---

## 📈 Keşifsel Veri Analizi (EDA)
Proje boyunca aşağıdaki görseller oluşturulmuştur:
1. **Train Setinde Segmentation Dağılımı**
2. **Cinsiyet Dağılımı (Train)**
3. **Sayısal Değişkenlerin Korelasyon Matrisi**
4. **Profession Dağılımı Segmentasyona Göre**
5. **Confusion Matrix (Validation Set)**
6. **Özellik Önem Sıralaması (RandomForest)**

Her grafik detaylı olarak raporda analiz edilmiştir.

---

## 🤖 Modelleme ve Eğitim

### Kullanılan Model
- **RandomForestClassifier:** 
  - Avantajları: Hızlı ve doğru, hem kategorik hem sayısal verilerde güçlü performans.
  - Optimizasyon: `GridSearchCV` ile en iyi parametreler belirlendi (\texttt{max_depth: 10, n_estimators: 200}).

### Eğitim Sonuçları
- **Doğruluk (Accuracy):** %53
- **Değerlendirme Metrikleri:**
  - **Precision, Recall, F1-Score**: Segmentasyon performansı detaylı olarak raporlanmıştır.
- **Confusion Matrix:** D segmenti net bir şekilde sınıflandırılmış, A-B segmentlerinde hata oranı yüksektir.

---

## 🔍 Sonuçların Analizi
- **Başarı:** Veri setinin karmaşık yapısına rağmen orta düzeyde bir doğruluk elde edilmiştir.
- **Hata Analizi:** 
  - A ve B segmentleri arasında karışıklık gözlemlenmiştir.
  - D segmenti model tarafından net bir şekilde ayrılmıştır.

### Öneriler:
- Ek özellikler (\textit{feature engineering}) ile performans artırılabilir.
- Alternatif modeller (ör. XGBoost, LightGBM) ile karşılaştırma yapılabilir.

---

## 🚀 Kullanılan Teknolojiler ve Araçlar
- **Python Kütüphaneleri:**
  - `pandas`, `numpy`: Veri analizi ve işleme
  - `matplotlib`, `seaborn`: Görselleştirme
  - `scikit-learn`: Modelleme ve değerlendirme
- **LaTeX:** Akademik rapor yazımı
- **Kaggle API:** Veri indirme ve yarışma dosyalarını yönetme

---

## 📂 Rapor ve Sunum
Proje raporu LaTeX kullanılarak oluşturulmuş, analiz sonuçları ve görseller rapora entegre edilmiştir. 
Rapora [buradan erişebilirsiniz](https://github.com/SleevelessTime/customer-segmentation-web-app/blob/main/python/Veri_Madencili%C4%9Fi_Latex.pdf).

---

## 👥 Proje Ekibi
- **Oğuzhan Cem Yücel** (oguzhancemyucel21@istanbularel.edu.tr)
- **Can Çebi** (cancebi21@istanbularel.edu.tr)

---

## 📚 Kaynaklar
- Kaggle Customer Segmentation Dataset: [Dataset Link](https://www.kaggle.com/datasets/vetrirah/customer)
- Scikit-Learn Dokümantasyonu: [Scikit-Learn](https://scikit-learn.org/stable/)