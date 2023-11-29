var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");
var button = document.getElementById("random");

// show the default color.
body.style.background = "linear-gradient(to right," + color1.value + "," + color2.value + ")";

function changeBackground() {
    body.style.background = "linear-gradient(to right," + color1.value + "," + color2.value + ")";
    css.textContent = body.style.background + ";";
}

function getRandomColor() {
    // Generate a random hex color code
    return '#' + Math.floor(Math.random()*16777215).toString(16);
}

function changebgRandomly() {
    body.style.background = "linear-gradient(to right," + getRandomColor() + "," + getRandomColor() + ")";
    css.textContent = body.style.background + ";";
}

color1.addEventListener("input", changeBackground);
color2.addEventListener("input", changeBackground);
button.addEventListener("click", changebgRandomly);
