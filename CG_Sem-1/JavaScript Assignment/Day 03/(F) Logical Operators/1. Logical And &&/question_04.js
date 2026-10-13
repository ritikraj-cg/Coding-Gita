let marks=75
let attendence=80
let passingMarks=65
let requiredAttendence=70
let isPassed=marks>=passingMarks && attendence>=requiredAttendence
console.log(isPassed)

if(marks>=passingMarks && attendence>=requiredAttendence){
    console.log("Passed")
}
else{
    console.log("Not Passed")
}