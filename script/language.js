const translations = {
    en: {
        languagetext: "Language:",
        title: "Customer Segmentation Project",
        aboutTitle: "About the Project",
        aboutText: "This project aims to segment customers based on their behaviors and characteristics. It allows businesses to better understand their customers and target them more effectively. " +
            "Customer segmentation helps companies identify key groups within their audience, such as high-value customers or those with specific preferences. With this understanding, businesses can personalize their marketing strategies, optimize product offerings, and enhance customer satisfaction. " +
            "By leveraging data-driven insights, this project enables organizations to make informed decisions, improve customer retention, and maximize overall profitability.",
        dataMiningTitle: "What is Data Mining?",
        dataMiningText: "Data mining is the process of extracting meaningful patterns, trends, and insights from large and complex datasets. With the rapid increase in digitalization, the amount of data is growing rapidly, making its proper analysis critical for businesses. " +
            "Data mining utilizes statistical methods, artificial intelligence, and machine learning algorithms to analyze data and support decision-making processes. For example, e-commerce companies use it to understand customer habits, while hospitals leverage it to improve disease diagnosis. The financial sector uses data mining to detect fraud and manage risks. " +
            "This process not only analyzes past data but also helps predict the future, enabling businesses to take proactive steps. Data mining stands out as a strategic guide in many sectors such as marketing, healthcare, finance, and education. Its essence lies in asking the right questions and making data meaningful. The value of data is determined by our ability to interpret it.",
        homeLink: "Home",
        aboutLink: "About",
        dataMiningLink: "Data Mining",
        footerText: "&copy; 2024 Customer Segmentation Project. All rights reserved."
    },
    tr: {
        languagetext: "Dil:",
        title: "Müşteri Segmentasyonu Projesi",
        aboutTitle: "Proje Hakkında",
        aboutText: "Bu proje, müşterileri davranışlarına ve özelliklerine göre segmentlere ayırmayı amaçlar. Böylece, işletmelerin müşteri tabanlarını daha derinlemesine anlamalarına ve onları daha etkili bir şekilde hedeflemelerine yardımcı olur. " +
            "Müşteri segmentasyonu, şirketlerin hedef kitlelerinde yüksek değerli müşteriler veya belirli tercihlere sahip olanlar gibi ana grupları tanımlamalarına olanak tanır. Bu anlayışla, işletmeler pazarlama stratejilerini kişiselleştirebilir, ürün tekliflerini optimize edebilir ve müşteri memnuniyetini artırabilir. " +
            "Veri odaklı içgörülerden yararlanarak, bu proje organizasyonların bilinçli kararlar almalarını, müşteri sadakatini artırmalarını ve genel karlılığı maksimize etmelerini sağlar.",
        dataMiningTitle: "Veri Madenciliği Nedir?",
        dataMiningText: "Veri madenciliği, büyük ve karmaşık veri setlerinden anlamlı desenler, trendler ve içgörüler elde etme sürecidir. Dijitalleşme ile birlikte veri miktarı hızla artarken, bu verilerin doğru analiz edilmesi işletmeler için kritik hale gelmiştir. " +
            "Veri madenciliği, istatistiksel yöntemler, yapay zeka ve makine öğrenimi algoritmaları kullanarak verileri analiz eder ve karar süreçlerini destekler. Örneğin, e-ticaret şirketleri müşteri alışkanlıklarını anlamak, hastaneler ise hastalık teşhislerini iyileştirmek için bu yöntemlerden faydalanır. Finans sektörü ise dolandırıcılığı tespit etmek ve riskleri yönetmek için veri madenciliğini kullanır. " +
            "Bu süreç yalnızca geçmiş verileri analiz etmekle kalmaz, geleceği tahmin ederek işletmelerin proaktif adımlar atmasına da olanak tanır. Veri madenciliği, pazarlama, sağlık, finans ve eğitim gibi birçok sektörde stratejik bir rehber olarak öne çıkar. Özü, doğru sorular sormak ve verileri anlamlı hale getirmektedir. Verilerin değerini, onları anlamlandırma yeteneğimiz belirler.",
        homeLink: "Ana Sayfa",
        aboutLink: "Hakkında",
        dataMiningLink: "Veri Madenciliği",
        footerText: "&copy; 2024 Müşteri Segmentasyonu Projesi. Tüm hakları saklıdır."
    }
};

function changeLanguage() {
    const selectedLang = document.getElementById('language').value;

    // Dil tercihini localStorage'a kaydet
    localStorage.setItem('selectedLang', selectedLang);

    // Metinleri güncelle
    document.getElementById('title').textContent = translations[selectedLang].title;
    document.getElementById('about-title').textContent = translations[selectedLang].aboutTitle;
    document.getElementById('about-text').textContent = translations[selectedLang].aboutText;
    document.getElementById('data-mining-title').textContent = translations[selectedLang].dataMiningTitle;
    document.getElementById('data-mining-text').textContent = translations[selectedLang].dataMiningText;
    document.getElementById('language-text').textContent = translations[selectedLang].languagetext;
    
    // Navbar bağlantı metinlerini güncelle
    document.getElementById('home-link').textContent = translations[selectedLang].homeLink;
    document.getElementById('about-link').textContent = translations[selectedLang].aboutLink;
    document.getElementById('data-mining-link').textContent = translations[selectedLang].dataMiningLink;

    // Footer metnini güncelle
    document.getElementById('footer-text').innerHTML = translations[selectedLang].footerText;

    // Seçim kutusunu doğru dile ayarla
    document.getElementById('language').value = selectedLang;
}

// Sayfa yüklendiğinde varsayılan dili ayarla
document.addEventListener('DOMContentLoaded', () => {
    // localStorage'dan önceki dil tercihini al
    const selectedLang = localStorage.getItem('selectedLang') || 'tr'; // Varsayılan olarak 'tr' dilini kullan

    // Dil seçim kutusunu ayarla ve metinleri değiştir
    document.getElementById('language').value = selectedLang;
    changeLanguage(); // Varsayılan metinleri ayarla
});
