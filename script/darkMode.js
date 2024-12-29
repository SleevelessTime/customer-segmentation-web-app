function toggleDarkMode() {
    const themeStyle = document.getElementById('theme-style');
    const cardStyle = document.getElementById('card-style'); // Kart stili için link etiketi
    const graphStyle = document.getElementById('graph-style'); // Grafik stili için link etiketi
    const darkModeBtn = document.getElementById('dark-mode-btn');
    const defaultStyle = 'style/indexStyle.css';
    const darkStyle = 'style/darkModeStyle.css';
    const defaultCardStyle = 'style/cardStyle.css';
    const darkCardStyle = 'style/darkModeCardStyle.css';
    const defaultGraphStyle = 'style/graphStyle.css';
    const darkGraphStyle = 'style/darkGraphStyle.css';

    // Gece modu kontrolü
    if (themeStyle.getAttribute('href') === defaultStyle) {
        themeStyle.setAttribute('href', darkStyle); // Gece modu stili
        cardStyle.setAttribute('href', darkCardStyle); // Kart gece modu stili
        graphStyle.setAttribute('href', darkGraphStyle); // Grafik gece modu stili
        localStorage.setItem('darkMode', 'enabled');
        darkModeBtn.innerText = 'Işık Modu';
    } else {
        themeStyle.setAttribute('href', defaultStyle); // Normal stil
        cardStyle.setAttribute('href', defaultCardStyle); // Kart normal stili
        graphStyle.setAttribute('href', defaultGraphStyle); // Grafik normal stili
        localStorage.setItem('darkMode', 'disabled');
        darkModeBtn.innerText = 'Gece Modu';
    }
}

// Sayfa yüklendiğinde kullanıcı tercihini uygula
document.addEventListener('DOMContentLoaded', () => {
    const themeStyle = document.getElementById('theme-style');
    const cardStyle = document.getElementById('card-style'); // Kart stili için link etiketi
    const graphStyle = document.getElementById('graph-style'); // Grafik stili için link etiketi
    const darkModeBtn = document.getElementById('dark-mode-btn');
    const darkModePreference = localStorage.getItem('darkMode');
    const defaultStyle = 'style/indexStyle.css';
    const darkStyle = 'style/darkModeStyle.css';
    const defaultCardStyle = 'style/cardStyle.css';
    const darkCardStyle = 'style/darkModeCardStyle.css';
    const defaultGraphStyle = 'style/graphStyle.css';
    const darkGraphStyle = 'style/darkGraphStyle.css';

    // Kullanıcının tercihini kontrol et ve uygula
    if (darkModePreference === 'enabled') {
        themeStyle.setAttribute('href', darkStyle);
        cardStyle.setAttribute('href', darkCardStyle);
        graphStyle.setAttribute('href', darkGraphStyle); // Grafik gece modu stilini uygula
        darkModeBtn.innerText = 'Işık Modu';
    } else {
        themeStyle.setAttribute('href', defaultStyle);
        cardStyle.setAttribute('href', defaultCardStyle);
        graphStyle.setAttribute('href', defaultGraphStyle); // Grafik normal stilini uygula
        darkModeBtn.innerText = 'Gece Modu';
    }
});
