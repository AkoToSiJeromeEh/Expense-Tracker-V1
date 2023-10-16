
let monthlyExpenses = document.getElementById("monthly-expenses");
let monthlyIncomes = document.getElementById('monthly-incomes');

let totalBalance = document.getElementById('total-bal')
const progressBar = document.getElementById("progress-bar");
const warningBalance = document.getElementById("warning-balance");

let expenses =  monthlyExpenses.innerHTML;
let CurrentMonthlyIncomes = monthlyIncomes.innerHTML;

const getCurrentMoney = (expenses, currentMonthlyIncome) => {

	return totalBalance.innerHTML = `$${currentMonthlyIncome - expenses}`
}
const warningBalances = (value, element) => {
	let message, color;
  
	if (value >= 100) {
	  message = '100% of your Income has been deducted! Poor Guy.';
	  color = 'red';
	} else if (value >= 80) {
	  message = '80-99% of your Income has been deducted!';
	  color = 'yellow';
	} else if (value >= 50) {
	  message = '50-79% of your Income has been deducted!';
	  color = 'orange';
	} else {
	  message = 'Less than 50% of your Income has been deducted.';
	  color = 'green';
	}
	element.innerHTML = message;
	element.style.color = color;
	element.style.fontWeight = 'bolder';
  };
  
const progressBarCalc = () => {
  const progressMove = (expenses / CurrentMonthlyIncomes) * 100;
  console.log(progressMove)
  progressBar.style.width = `${progressMove}%`;
  warningBalances(progressMove , warningBalance);
};
getCurrentMoney(expenses , CurrentMonthlyIncomes)
progressBarCalc();
