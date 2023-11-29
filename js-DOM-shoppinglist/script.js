var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");

function createListElement() {
	var div = document.createElement("div");
	var li = document.createElement("li");
	var delButton = document.createElement("button");
	div.classList.add("wrapper");
	ul.appendChild(div);
	div.append(li, delButton);
	li.classList.add("taskClass");
	li.appendChild(document.createTextNode(input.value));
	input.value = "";
	delButton.classList.add("delete");
	delButton.innerHTML='Del';
}

function addDoneClass(event) {
    if (event.target.tagName === 'LI') {
        event.target.classList.toggle('done');
    }
}

function deleteListElement(event) {
	if (event.target.className === "delete"){
		event.target.parentElement.remove();
	}
}

function handleUlClick (event) {
	addDoneClass(event);
	deleteListElement(event);
}

function inputLength() {
    return input.value.length;
}

function addListAfterClick() {
    if (inputLength() > 0){
        createListElement();
    }
}

function addListAfterKeydown(event) {
    if (inputLength() > 0 && event.key === "Enter") {
        createListElement();
    }
}

button.addEventListener("click", addListAfterClick);
input.addEventListener("keydown", addListAfterKeydown);
// done
ul.addEventListener('click', handleUlClick);
