let passwordCorrect=true
let otpValid=false
let isLoginAllowed=passwordCorrect || otpValid;
console.log(isLoginAllowed)

if(isLoginAllowed){
    console.log("Login Allowed")
}
else{
    console.log("Login Not Allowed")
}