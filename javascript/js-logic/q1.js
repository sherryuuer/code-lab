// Question 1: Clean the room function: given an input of [1,2,4,591,392,391,2,5,10,2,1,1,1,20,20], make a function that organizes these into individual array that is ordered. For example answer(ArrayFromAbove) should return: [[1,1,1,1],[2,2,2], 4,5,10,[20,20], 391, 392,591]. Bonus: Make it so it organizes strings differently from number types. i.e. [1, "2", "3", 2] should return [[1,2], ["2", "3"]]

const input = [1,2,4,591,392,391,2,5,10,2,1,1,1,20,20];
input.sort(function(a, b){return a - b});

// [1, 1, 1, 1, 2, 2, 2, 4, 5, 10, 20, 20, 391, 392, 591]
let output = [];
for ( i = 0; i < input.length; i ++ ) {
    if ( i === 0 ) {
        if ( input[i] === input[i + 1] ) {
            output.push([input[i]]);
        }
        else {
            output.push(input[i]);
        }
    }
    else if ( i === input.length - 1 ) {
        if ( input[i] === input[i - 1] ) {
            output[output.length - 1].push(input[i]);
        }
        else {
            output.push(input[i]);
        }
    }  
    else {
        if (input[i] === input[i - 1]) {
            output[output.length - 1].push(input[i]);
        }
        else {
            if ( input[i] !== input[i + 1] ) {
                output.push(input[i]);
            }
            else {
                output.push([input[i]]);
            } 
        }
    }
}
// code too long, try again!
// [1, 1, 1, 1, 2, 2, 2, 4, 5, 10, 20, 20, 391, 392, 591]
// by object
let output2 = {};
for ( i = 0; i < input.length; i ++ ) {
    let element = input[i];
    if ( element in output2 ) {
        output2[element] += 1;
    } else {
        output2[element] = 1;
    }
}
console.log(output2);

const uniqueArray = [...new Set(input)];
console.log(uniqueArray);
let array = []
uniqueArray.forEach( element => {
    if ( output2[element] > 1 ) {
        array.push(Array(output2[element]).fill(element));
    } else {
        array.push(element);
    }
})
console.log(array);


// another try!
function organizeArray(inputArray) {
    // 先将数组排序
    const sortedArray = inputArray.sort((a, b) => a - b);

    // 初始化结果数组
    const resultArray = [];

    // 遍历排序后的数组
    let currentNumber; // undefined
    let currentSubarray; // undefined

    for (const number of sortedArray) {
        if (number === currentNumber) {
            // 如果当前数字与前一个数字相同，则将其添加到当前子数组
            currentSubarray.push(number);
        } else {
            // 如果当前数字与前一个数字不同，则创建一个新的子数组
            currentNumber = number;
            currentSubarray = [number];
            resultArray.push(currentSubarray);
        }
    }

    let result = [];
    for (const arr of resultArray) {
        if ( arr.length > 1 ) {
            result.push(arr);
        } else {
            result.push(arr[0]);
        }
    }
    return result;
}

const inputArray = [1, 2, 4, 591, 392, 391, 2, 5, 10, 2, 1, 1, 1, 20, 20];
const result = organizeArray(inputArray);

console.log(result);

