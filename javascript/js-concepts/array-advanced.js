// Complete the below questions using this array:
const array = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"]
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"]
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"]
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"]
  },

];

//Create an array using forEach that has all the usernames with a "!" to each of the usernames
const array2 = []
array.forEach((user) => {
  array2.push(user.username = user.username + "!");
})
console.log(array2);
// OR
array.forEach(user => {
	let { username } = user;
	username = username + "!";
	array2.push(username);
})

//Create an array using map that has all the usernames with a "? to each of the usernames
const array3 = array.map(user => user.username + "?")
const maparray = array.map(user =>{
  let { username } = user;
  return username + "?";
})

//Filter the array to only include users who are on team: red
const array4 = array.filter(user => {
  let { username, team } = user;
  return team === "red";
})
console.log(array4)
// OR
const filterArray = array.filter(user => {
	return user.team === "red";
})
console.log(filterArray);


//Find out the total score of all users using reduce
const total = array.reduce((acc, user)=> {
  console.log(acc, user.score);
  return acc + user.score;
}, 0)
console.log("total", total);


// (1), what is the value of i?
// (2), Make this map function pure:
const arrayNum = [1, 2, 4, 5, 8, 9];
const newArray2 = arrayNum.map((num, i) => {
	return num * 2;
})

//BONUS: create a new list with all user information, but add "!" to the end of each items they own.
const newuserlist4 = array.map(user => {
  user.items = user.items.map(item => {
    return item + "!"
  });
  return user;
})
console.log(newuserlist4);


const answer = array.map(user => {
	user.items = user.items.map(item => {
		return item + "!"
	});
	return user;
})
console.log(answer);
