console.log(undefined === null)  // false 严格的相等
console.log(undefined == null)  // true

console.log(Number(null))  // 0
console.log(Number(undefined))  // NaN

// Symbol
// Create a symbol: "This is my first Symbol"
const sym = Symbol('This is my first Symbol');
