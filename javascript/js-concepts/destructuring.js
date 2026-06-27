// 解构
const obj = {
    player: "bobby",
    experience: 100,
    wizardLevel: false
}

// const player = obj.player;
// const experience = obj.experience;
// let wizardLevel = obj.wizardLevel;

const { player, experience } = obj;
let { wizardLevel } = obj;

const a = "Simon";
const b = true;
const c = "";

const obj2 = {a, b, c}
