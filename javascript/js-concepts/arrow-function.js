function add(a, b) {
    return a + b;
}

const add = (a, b) => a + b;

// default arguments
// default age to 10;
const isValidAge = (age = 10) => age;


// Arrow functions
const whereAmI = (username, location) => {
    if (username && location) {
        return "I am not lost";
    } else {
        return "I am totally lost!";
    }
}
