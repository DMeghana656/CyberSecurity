document.addEventListener("DOMContentLoaded", function () {
    console.log("Hybrid Security Dashboard Loaded");
 let hour = new Date().getHours();
    let greeting = "";
    if (hour < 12) {
        greeting = "Good Morning";
    }
    else if (hour < 18) {
        greeting = "Good Afternoon";
    }
    else {
        greeting = "Good Evening";
    }
    let greetingElement = document.getElementById("greeting");
    if (greetingElement) {
        greetingElement.innerHTML = greeting;
    }
let cards = document.querySelectorAll(".card");
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";
        setTimeout(() => {
            card.style.transition = "all 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0px)";
        }, index * 200);
    });
});
function updateDateTime() {
    let now = new Date();
    let dateTime = now.toLocaleString();
    let dateElement = document.getElementById("datetime");
    if (dateElement) {
        dateElement.innerHTML = dateTime;
    }
}
updateDateTime();
setInterval(updateDateTime, 1000);
setInterval(function () {
    console.log("Dashboard Refreshed");
    location.reload();
}, 30000);
document.addEventListener("mouseover", function (event) {
    if (event.target.classList.contains("card")) {
        event.target.style.transform = "scale(1.05)";
    }
});
document.addEventListener("mouseout", function (event) {
    if (event.target.classList.contains("card")) {
        event.target.style.transform = "scale(1)";
    }
});