// 使用函数表达式创建一个匿名函数
var anonymousFunction = function() {
    console.log("这是一个匿名函数。");
};
  
  // 调用匿名函数
anonymousFunction();


// 在点击按钮时执行匿名函数
document.getElementById("myButton").addEventListener("click", function() {
    console.log("按钮被点击了。");
});
  
  