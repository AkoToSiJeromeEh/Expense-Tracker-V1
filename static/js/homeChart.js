const imageBackgroundPattern = new Image();
imageBackgroundPattern.src = '../static/images/chart-pattern.jpg';

const ctx = document.getElementById('myChart').getContext('2d');

Chart.defaults.font.family = "Quicksand";
Chart.defaults.font.size = 14;
Chart.defaults.font.weight = 'bolder';
Chart.defaults.color = "#23ACE1";

const gradient = ctx.createLinearGradient(0, 0, 0, 600);
gradient.addColorStop(0, '#23ACE1');
gradient.addColorStop(0.2, '#E079C2');
gradient.addColorStop(0.4, '#CE69F5');
gradient.addColorStop(0.6, '#7A88F1');
gradient.addColorStop(0.8, '#CE69F5');
gradient.addColorStop(1, '#FF9668');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Days', 'Weeks', 'Monthly', 'Yearly'],
        datasets: [{
            label: 'Expenses',
            data: [110003, 100203, 320003, 200003],
            borderRadius: 30,
            barThickness: 10,
            backgroundColor: gradient,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                grid: {
                    display: false,
                }
            },
            x: {
                grid: {
                    display: false,
                }
            }
        },
		
    }
});

const chartContainer = document.getElementById('chart-section-hidden');
const chartContainerOrigStyle = chartContainer.style.display;
const chartToggler = document.getElementById('chart-btn-toggler');
const chartTogglerOrigContext = chartToggler.textContent; 

let isToggle = true;

const showChart = () => {
    if (isToggle) {

        chartContainer.style.display = 'block';
        chartToggler.textContent = 'Close Chart';
    } else {
        chartContainer.style.display = chartContainerOrigStyle;
        chartToggler.textContent = chartTogglerOrigContext;
    }
    isToggle = !isToggle;
   
};

chartToggler.addEventListener('click', showChart);
