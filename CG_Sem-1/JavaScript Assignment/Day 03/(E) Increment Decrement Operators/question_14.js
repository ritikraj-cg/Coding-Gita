let p = 3;
let q = p++ + ++p + p;
console.log(p, q);

// p will be 5
// p++ will 4 also
// ++p=5
// // 4+5+3=12
// but output 13, i dont understand.