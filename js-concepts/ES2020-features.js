// 1,BigInt 
// used when larger than this lagest number.
Number.MAX_SAFE_INTEGER
typeof 1n; // Bigint

// 2,optional chaining operator ?
let Sally_pokemon = {
    pikachu: {
        species: "Mouse Pokemon",
        height: 0.4,
        weight: 6,
        power: 0 // ""//false
    }
}

if (Sally_pokemon.pikachu && Sally_pokemon.pikachu.weight){
    let weight = Sally_pokemon.pikachu.weight
    console.log(weight);
}
// instead of doing the loooooong if.do this:
let weight = Sally_pokemon?.pikachu?.weight
console.log(weight);

// 3,nullish coalescing operator ??
let power = Sally_pokemon?.pikachu?.power || "no power" // || is or 判断的是真假ture false
console.log(power);

let power2 = Sally_pokemon?.pikachu?.power ?? "no power" // ??判断的是是否存在 null表示不存在！
console.log(power2);


// Exercise 3: Clean up this code using optional chaining
let will_pokemon = {
    pikachu: {
        species: 'Mouse Pokemon',
        height: 0.4,
        weight: 6,
        power: 'lightning',
        friend: { 
            charizard: {
                species: 'Dragon Pokemon',
                height: 1.7,
                weight: 90.5,
                power: 'fire'
            }
        }
    }
}

let andrei_pokemon = {
    raichu: {
        species: 'Mouse Pokemon',
        height: 0.8,
        weight: 30,
        power: ''
    }
}

if (andrei_pokemon?.raichu && will_pokemon?.pikachu?.friend?.charizard) {
        console.log('fight!')
    } else {
        console.log('walk away...')
    }


// Exercise 4: What do these each output?
console.log(false ?? 'hellooo') // false
console.log(null ?? 'hellooo') // null xxx hellooo
console.log(null || 'hellooo') // hellooo
console.log((false || null) ?? 'hellooo') // null xxx hellooo
console.log(null ?? (false || 'hellooo')) // null xxx hellooo
// 因为null不存在
