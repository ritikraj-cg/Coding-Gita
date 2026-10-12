let x = 10;
let y = x++;
let z = ++x;
console.log(x, y, z)

//The result is x=12 because it increase two times. y=10 because its take x value and x get +1,
// z=12 because x increase 2 times and its pre-increment so value will be changed.