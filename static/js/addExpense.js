const allTabContents = document.getElementsByClassName("tab-content");
const buttonTabs = document.querySelectorAll(".button-tab");
const sucessInsert = document.getElementById('sucessInsert');
const sucessRemind = document.getElementById('sucess-remind');

buttonTabs.forEach(function (tabButton, index) {
  tabButton.addEventListener("click", function () {
    
    [...allTabContents].forEach((content) => (content.style.display = "none"));

    buttonTabs.forEach(function (btn) {
      btn.classList.remove("active");
      btn.style.color = "white";
    });
    allTabContents[index].style.display = "block";
    tabButton.classList.add("active");
  });
});
buttonTabs[0].click();

const resetSucess = () => {
  
    setInterval(() => {

        sucessInsert.innerHTML = ' ';
        sucessRemind.innerHTML = ' ';
    } , 5000)
}
resetSucess()