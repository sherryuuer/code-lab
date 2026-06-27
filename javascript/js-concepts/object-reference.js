let obj = {
    a: "a",
    b: "b",
    c: {deep: "try copy me"}
}

// shallow copy 浅拷贝只拷贝第一层
let clone = Object.assign({}, obj);
let clone2 = {...obj}
// deep copy，but this will take long time.
let superClone = JSON.parse(JSON.stringify(obj))

obj.c.deep = "wwww";
console.log(obj);
console.log(clone);
console.log(clone2);


// {a: 'a', b: 'b', c: {…}}
// {a: "a", b: "b", c: {deep: 'wwww'}}
