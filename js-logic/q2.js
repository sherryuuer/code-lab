// Question 2: Write a javascript function that takes an array of numbers and a target number. The function should find two different numbers in the array that, when added together, give the target number. For example: answer([1,2,3], 4)should return [1,3]
function twoSum(arr, total) {
    const dict = {};
    for (let i = 0; i < arr.length; i ++) { 
        num = total - arr[i]
        if (num in dict) {
            return [num, arr[i]];
        }else{
            dict[arr[i]] = i;
        }
    }
    return null;
}

let result = twoSum([1,2,3], 4);
console.log(result)
