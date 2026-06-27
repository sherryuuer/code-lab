//1
for (let i = 0; i < basket.length; i++) {
    console.log(basket[i]);
  }
  
  //2
  basket.forEach(item => {
    console.log(item);
  })
// for of ..interating array, strings
const basket = ["apple", "banana"] 
for (item of basket) {
    console.log(item);
}
// for in ..objects  enumerating to see the properties
const detailedbasket = {
    apples: 5,
    bananas: 6, 
}
for (item in detailedbasket) {
    console.log(item);
}
//// exchange:
for (item of detailedbasket) {
    console.log(item);
}// 会报错
for (item in basket) {
    console.log(item);
}// 输出index 0， 1


// exercise
// Question #1:
// create a function called biggestNumberInArray() that takes
// an array as a parameter and returns the biggest number.
// biggestNumberInArray([-1,0,3,100, 99, 2, 99]) should return 100;
// Use at least 3 different types of javascript loops to write this:
const array = [-1,0,3,100, 99, 2, 99] // should return 100
const array2 = ['a', 3, 4, 2] // should return 4
const array3 = [] // should return 0

function biggestNumberInArray(arr) {
    if (arr.length === 0){
        return 0;
    }
    let maxNum = -Infinity;
    for ( num of arr ){
        if (num >= maxNum){
            maxNum = num;
        } 
    }
    return maxNum;
}

function biggestNumberInArray2(arr) {
    if (arr.length === 0){
        return 0;
    }
    let maxNum = -Infinity;
    arr.forEach(num => {
        if (num >= maxNum){
            maxNum = num;
      }})
    return maxNum;
}

function biggestNumberInArray3(arr) {
    if (arr.length === 0){
        return 0;
    }
    let maxNum = -Infinity;
    for (let i = 0; i < arr.length; i++ ){
        if (arr[i] >= maxNum){
            maxNum = arr[i];
        }
    }
    return maxNum
}


// Question #2:
// Write a function checkBasket() that lets you know if the item is in the basket or not
amazonBasket = {
  glasses: 1,
  books: 2,
  floss: 100
}

function checkBasket(basket, lookingFor) {
    for (item in basket){
        if (item === lookingFor){
            return true;
        }
    }
    return false;
}
