const allTabContents = document.getElementsByClassName("tab-content");
const buttonTabs = document.querySelectorAll(".button-tab");

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
