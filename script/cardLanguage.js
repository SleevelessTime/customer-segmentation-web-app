function changeLanguage() {
    const selectedLanguage = document.getElementById('language').value;

    // Dil tercihlerini localStorage'a kaydet
    localStorage.setItem('language', selectedLanguage);

    // Metinleri değiştirme
    if (selectedLanguage === 'en') {
        setEnglishText();
    } else {
        setTurkishText();
    }
}

// Sayfa yüklendiğinde, kullanıcı tercihini uygula
document.addEventListener('DOMContentLoaded', () => {
    const languagePreference = localStorage.getItem('language') || 'tr';  // Varsayılan olarak Türkçe
    document.getElementById('language').value = languagePreference;

    // Dil tercihini uygula
    if (languagePreference === 'en') {
        setEnglishText();
    } else {
        setTurkishText();
    }
});

// Türkçe metinler
function setTurkishText() {
    document.getElementById('title').innerText = 'Müşteri Segmentasyonu Projesi';
    document.getElementById('home-link').innerText = 'Ana Sayfa';
    document.getElementById('about-link').innerText = 'Hakkında';
    document.getElementById('data-mining-link').innerText = 'Veri Madenciliği';
    document.getElementById('language-text').innerText = 'Dil: ';

    document.getElementById('name1').innerText = 'Oğuzhan Cem Yücel';
    document.getElementById('role1').innerText = 'Yazılım Geliştiricisi';
    document.getElementById('about-title1').innerText = 'Hakkında';
    document.getElementById('about-text1').innerText = 'Ben Oğuzhan Cem Yücel, İstanbul Arel Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisiyim. Yazılım geliştirme, mobil uygulama geliştirme ve otomasyon gibi alanlara büyük bir ilgi duyuyorum. Teknolojiyi etkili kullanarak verimliliği artırmaya yönelik projelerde yer almayı hedefliyorum. Ayrıca, afet ve acil durum yönetimi konularına olan ilgimle, bu alanda da aktif roller üstleniyorum.';

    document.getElementById('name2').innerText = 'Can Çebi';
    document.getElementById('role2').innerText = 'Veri Bilimci';
    document.getElementById('about-title2').innerText = 'Hakkında';
    document.getElementById('about-text2').innerText = 'Ben Can Çebi, İstanbul Arel Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisi olarak, yazılım geliştirme ve altyapı yönetimi alanlarında kendimi geliştirmeye çalışan bir teknoloji meraklısıyım.';

    document.getElementById('footer-text').innerText = '© 2024 Müşteri Segmentasyonu Projesi. Tüm hakları saklıdır.';
}

// İngilizce metinler
function setEnglishText() {
    document.getElementById('title').innerText = 'Customer Segmentation Project';
    document.getElementById('home-link').innerText = 'Home';
    document.getElementById('about-link').innerText = 'About';
    document.getElementById('data-mining-link').innerText = 'Data Mining';
    document.getElementById('language-text').innerText = 'Language: ';

    document.getElementById('name1').innerText = 'Oğuzhan Cem Yücel';
    document.getElementById('role1').innerText = 'Software Developer';
    document.getElementById('about-title1').innerText = 'About';
    document.getElementById('about-text1').innerText = 'I am Oğuzhan Cem Yücel, a senior student in Computer Engineering at Istanbul Arel University. I am very interested in software development, mobile app development, and automation. I aim to participate in projects that increase efficiency through effective use of technology. I am also actively involved in disaster and emergency management.';

    document.getElementById('name2').innerText = 'Can Çebi';
    document.getElementById('role2').innerText = 'Data Scientist';
    document.getElementById('about-title2').innerText = 'About';
    document.getElementById('about-text2').innerText = 'I am Can Çebi, a senior student in Computer Engineering at Istanbul Arel University, trying to improve myself in software development and infrastructure management areas.';

    document.getElementById('footer-text').innerText = '© 2024 Customer Segmentation Project. All rights reserved.';
}
