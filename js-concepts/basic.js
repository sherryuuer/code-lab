// Control Flow
var username = "Billy";
if (username === "Billy") {
    alert("Hi, Billy");
} else {
    alert("Sorry, I don't know you.")
}


// 声明了变量却没有赋值
undefined


// string number alert prompt
var first = prompt("What is the first number?");
var second = prompt("What is the second number?");
var sum = Number(first) + Number(second);
alert("The sum is : " + sum);
// ; is the end of a expression.


// let和const
let y = 20; // 声明一个块级作用域（就是花括号）的变量
const z = 30; // 声明一个块级作用域的常量


// 块级作用域和变量声明
function example() {
    if (true) {
        var x = 10; // 不是块级作用域，会提升到函数作用域
        let y = 20; // 块级作用域
        const z = 30; // 块级作用域
    }
  
    console.log(x); // 10，因为 var 不是块级作用域
    // console.log(y); // 报错，y is not defined，因为 y 是块级作用域
    // console.log(z); // 报错，z is not defined，因为 z 是块级作用域
  }
  
example();
  


//Evaluate the below:
5 + "34" // "534"
5 - "4" // 1
10 % 5 // 0
5 % 10 // 5
"Java" + "Script" // "JavaScript"
" " + " " // "  "
" " + 0 // " 0"
true + true // 2
true + false // 1
false + true // 1 
false - true // -1
3 - 4 // -1
"Bob" - "bill" // NaN


//Evaluate the below comparisons:
5 >= 1 // true
0 === 1 // false
4 <= 1 // false
1 != 1 // false
"A" > "B" // false
"B" < "C" // true
"a" > "A" // true
"b" < "A" // false
true === false // false
true != true // false


// Make the string: "Hi There! It's "sunny" out" by using the + sign:
"Hi There! It's \"sunny\" out"
