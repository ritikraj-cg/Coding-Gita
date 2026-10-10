1. Check whether `"18" !== 18` returns true or false.

console.log("18" !== 18);  // true

2. Check if `0 !== false` and `null !== undefined`.

console.log(0 !== false);  // true
console.log(null !== undefined);  // true

4. Predict the output:

   console.log("" !== 0);  // true
   console.log(NaN !== NaN);  //true
 
5. Write a condition that checks if a variable `input` is strictly not equal to the string `"0"`.

if (input !== "0") {
  console.log("Input is not the string 0");
}