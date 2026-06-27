const addTo = x => y => x + y
var addToTen = addTo(10)
addToTen(3)  // 13

// closure
const first = () => {
    const greet = "hi";
    const second = () => {
        alert(greet);
    }
    return second;
}

const newFunc = first();
newFunc();

// 作用
// 保存私有变量
// 封装： 闭包可以用于创建私有变量，模拟类的封装性质。
// 在事件处理程序中使用闭包： 闭包可以用于在事件处理程序中保存状态。
function setupClick() {
    let count = 0;
    document.getElementById('myButton').addEventListener('click', function() {
      count++;
      console.log(`Button clicked ${count} times`);
    });
  }
setupClick();
  