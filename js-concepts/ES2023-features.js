// array
// findLast()
const element = Array.findLast(item => item.num > 0)
// filter and getlast in one line.

// findLastIndex()
const element2 = Array.findLastIndex(item => item.num > 0)
// filter and getlast index

// toReversed() 
Array.reverse() // 直接作用于原数组
Array.toReversed() // 不作用于原数组
// 其他还有toSorted(), toSpliced(index, remove x ele from index), 等

// with 不改变原数组
Array.with(index, xxx) // modify ele at index to be xxx
//-------------------------------------------------------------

const ztmMonsters = [
    {id: 1, monster: 'Mr. Mouse', level: 1},
    {id: 2, monster: 'Mac', level: 30},
    {id: 3, monster: 'Denodude', level: 17},
    {id: 4, monster: 'Pye', level: 5},
    ];
    
// Old Way
const advancedMonsters = ztmMonsters.filter(item => item.level > 15)
console.log(advancedMonsters)
console.log(advancedMonster[advancedMonsters.length - 1])


// Using findLast()
const lastMonster = ztmMonsters.findLast(item => item.level > 15);
console.log(lastMonster);
// Using findLastIndex()
const lastMonsterIndex = ztmMonsters.findLastIndex(item => item.level > 15);
console.log(lastMonsterIndex);


const ztmMonstersList = ['Mr. Mouse', 'Mac', 'Denodude', 'Pye'];

//Using reverse()
const reverseMonsters = ztmMonstersList.reverse();
console.log(ztmMonstersList) 
console.log(reverseMonsters) 

//using toReversed()
const reversedMonstersTo = ztmMonstersList.toReversed();
console.log(ztmMonstersList) 
console.log(reversedMonstersTo)

//Using toSorted()
const sortedMonstersTo = ztmMonstersList.toSorted();
console.log(ztmMonstersList) 
console.log(sortedMonstersTo)

//Using toSpliced()
const spliceMonstersTo = ztmMonstersList.toSpliced(2, 1);
console.log(ztmMonstersList) 
console.log(spliceMonstersTo)

//Old Way
ztmMonstersList[1] = 'Gost';
console.log(ztmMonstersList)

// Using with()
const withMonsters = ztmMonstersList.with(1, 'Gost');
console.log(ztmMonstersList) 
console.log(withMonsters)
