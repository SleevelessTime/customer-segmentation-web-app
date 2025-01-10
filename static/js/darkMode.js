function toggleDarkMode() {
    const themeStyle = document.getElementById('theme-css');
    const cardStyle = document.getElementById('card-css');
    const graphStyle = document.getElementById('graph-css');
    const darkModeBtn = document.getElementById('dark-mode-btn');

    // Sabit (mutlak) yollar
    const defaultStyle = "/static/css/indexStyle.css";
    const darkStyle = "/static/css/darkModeStyle.css";
    const defaultCardStyle = "/static/css/cardStyle.css";
    const darkCardStyle = "/static/css/darkModeCardStyle.css";
    const defaultGraphStyle = "/static/css/graphStyle.css";
    const darkGraphStyle = "/static/css/darkGraphStyle.css";

    // Geçerli tema hangisi
    const currentTheme = themeStyle.getAttribute('href');

    // Değiştir
    if (currentTheme === defaultStyle) {
        // Gece modu
        themeStyle.setAttribute('href', darkStyle);
        cardStyle.setAttribute('href', darkCardStyle);
        graphStyle.setAttribute('href', darkGraphStyle);
        localStorage.setItem('darkMode', 'enabled');
        darkModeBtn.innerText = 'Işık Modu';
    } else {
        // Aydınlık mod
        themeStyle.setAttribute('href', defaultStyle);
        cardStyle.setAttribute('href', defaultCardStyle);
        graphStyle.setAttribute('href', defaultGraphStyle);
        localStorage.setItem('darkMode', 'disabled');
        darkModeBtn.innerText = 'Gece Modu';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const themeStyle = document.getElementById('theme-css');
    const cardStyle = document.getElementById('card-css');
    const graphStyle = document.getElementById('graph-css');
    const darkModeBtn = document.getElementById('dark-mode-btn');

    const defaultStyle = "/static/css/indexStyle.css";
    const darkStyle = "/static/css/darkModeStyle.css";
    const defaultCardStyle = "/static/css/cardStyle.css";
    const darkCardStyle = "/static/css/darkModeCardStyle.css";
    const defaultGraphStyle = "/static/css/graphStyle.css";
    const darkGraphStyle = "/static/css/darkGraphStyle.css";

    const darkModePreference = localStorage.getItem('darkMode');

    if (darkModePreference === 'enabled') {
        themeStyle.setAttribute('href', darkStyle);
        cardStyle.setAttribute('href', darkCardStyle);
        graphStyle.setAttribute('href', darkGraphStyle);
        darkModeBtn.innerText = 'Işık Modu';
    } else {
        themeStyle.setAttribute('href', defaultStyle);
        cardStyle.setAttribute('href', defaultCardStyle);
        graphStyle.setAttribute('href', defaultGraphStyle);
        darkModeBtn.innerText = 'Gece Modu';
    }
});
