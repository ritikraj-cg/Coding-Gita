let val = 0;
val = val++ + ++val;
console.log(val);

// val=0
// val++ ALSO 0
// ++val=2
// val++ + ++val = 0 + 2 = 2