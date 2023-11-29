const compose = (f, g) => (a) => f(g(a));
const sum = (num) => num + 1;
compose(sum, sum)(5);
// 7

//Composing: What does the last line return?
const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
compose(add1, add5)(10)
// compose(add1, add5)(10) = add1(add5(10)) = add1(10 + 5) = add1(15) = 16



// 也就是高阶函数
// 定义两个简单的函数
const double = x => x * 2;
const square = x => x * x;

// 使用 compose 组合函数
const compose = (f, g) => x => f(g(x));

// 组合 double 和 square
const doubleThenSquare = compose(square, double);

console.log(doubleThenSquare(3)); // 输出: 36，先 double 再 square
