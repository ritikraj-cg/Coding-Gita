let levelOpenScore = 1000;
let userScore=900;
let timeBonus = true;
let isGameLevelOpen = levelOpenScore < userScore || timeBonus;
console.log(isGameLevelOpen)