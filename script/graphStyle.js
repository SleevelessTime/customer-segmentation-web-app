function showGraph(type) {
    const ctx = document.getElementById('graphCanvas').getContext('2d');

    // Önceki grafiği temizle
    if (window.myChart) {
        window.myChart.destroy();
    }

    // Grafik verilerini belirle
    let chartData;
    let chartOptions;
    let chartType;

    switch (type) {
        case "scatter-4-values":
            chartType = "scatter";
            chartData = {
                datasets: [{
                    label: '4 Değerli Dağılım',
                    data: [
                        { x: 5, y: 7 },
                        { x: 10, y: 15 },
                        { x: 20, y: 30 },
                        { x: 25, y: 35 }
                    ],
                    backgroundColor: 'rgba(75, 192, 192, 0.6)'
                }]
            };
            chartOptions = {
                scales: {
                    x: { title: { display: true, text: 'X Değeri' } },
                    y: { title: { display: true, text: 'Y Değeri' } }
                }
            };
            break;

        case "confusion-matrix":
            chartType = "bar";
            chartData = {
                labels: ['True Positive', 'False Positive', 'True Negative', 'False Negative'],
                datasets: [{
                    label: 'Confusion Matrix',
                    data: [50, 10, 35, 5],
                    backgroundColor: ['#4caf50', '#f44336', '#2196f3', '#ffc107']
                }]
            };
            chartOptions = {
                indexAxis: 'y',
                plugins: {
                    legend: { display: true }
                }
            };
            break;

        case "feature-importance":
            chartType = "bar";
            chartData = {
                labels: ['Feature A', 'Feature B', 'Feature C', 'Feature D'],
                datasets: [{
                    label: 'Özellik Önem Skorları',
                    data: [0.9, 0.8, 0.7, 0.6],
                    backgroundColor: 'rgba(153, 102, 255, 0.6)'
                }]
            };
            chartOptions = {
                plugins: {
                    legend: { display: true }
                }
            };
            break;

        default:
            chartType = "line";
            chartData = {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                    label: 'Örnek Grafik',
                    data: [5, 10, 15, 20, 25],
                    borderColor: 'rgba(255, 99, 132, 0.6)',
                    fill: false
                }]
            };
            chartOptions = {};
    }

    // Yeni grafik oluştur
    window.myChart = new Chart(ctx, {
        type: chartType,
        data: chartData,
        options: chartOptions
    });
}
