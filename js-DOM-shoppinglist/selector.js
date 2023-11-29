document.getElementById();
document.getElementsByClassName();
document.getElementsByTagName();

document.querySelector();
document.querySelectorAll();
document.querySelectorAll("li").getAttribute("random");
document.querySelectorAll("li").setAttribute("random", "notrandom");

document.querySelector("h1").style;
document.querySelector("h1").style.background = "yellow";

// can change the css
document.querySelector("li").classList.add("cooltitle");
document.querySelector("li").classList.remove("cooltitle");

// It's important to cache selectors in variables!!
var li = document.querySelector("li");
li.className = "cooltitle";

li.innerHTML = "<strong>text";

li.parentElement.parentElement.children;
