//Currying: What does the last line return?
const sum = (a, b) => a + b
const curriedSum = (a) => (b) => a + b
curriedSum(30)(1)
// curriedSum(30): (b) = 30 + b
// res = 31


//Currying: What does the last line return?
const sum = (a, b) => a + b
const curriedSum = (a) => (b) => a + b
const add5 = curriedSum(5)
add5(12)
// add5 = curriedSum(b) = 5 + b
// add5(12) = 5 + 12 = 17

// 柯里化（Currying）是一种将接受多个参数的函数转变成一系列接受单一参数的函数的技术。通过柯里化，你可以部分应用函数，并在稍后提供剩余参数。这种技术是由数学家 Haskell Curry 命名的。
// 有助于创建更灵活和可组合的函数。柯里化的好处之一是它使得函数更容易被复用，并且在组合多个函数时更加方便。
