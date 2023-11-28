// Create an object and an array which we will use in our facebook exercise. 
// 1. Create an object that has properties "username" and "password". Fill those values in with strings.
var userdata = {
    username: "Andy",
    password: "likeyoubaby",
};

// 2. Create an array which contains the object you have made above and name the array "database".
var database = [
    {
    username: "Andy",
    password: "likeyoubaby",
    }
];
// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".
var newsfeed = [
    {
        username: "Jerry",
        timeline: "What a big humberger!",
    },
    {
        username: "Sally",
        timeline: "I just cant stop learning!!",
    },
    {
        username: "Pandy",
        timeline: "What should I eat tonight??",
    },
];

var usernamePrompt = prompt("What is your name? ");
var passwordPrompt = prompt("What is your password? ");


// bad answer
function signIn(username, password){
    for (var i=0; i<database.length; i++){
        if (username === database[i]){
            if (password === database[i].password){
                console.log("Welcome back!");
                console.log(newsfeed);
                break;
            } else{
                alert("Password wrong!");
                break;
            }
        }
    }
}

signIn(usernamePrompt, passwordPrompt);


// good answer
function checkuser(username, password){
    for (var i=0; i<database.length; i++){
        if (username === database[i].username && password === database[i].password){
            return true;
        }
    }
    return false;
}

function signIn2(username, password){
        if (checkuser(username, password)){
            console.log(newsfeed);
        } else{
            console.log("sorry, your name or password is not right.")
        }
    }

console.log(signIn2(usernamePrompt, passwordPrompt));
