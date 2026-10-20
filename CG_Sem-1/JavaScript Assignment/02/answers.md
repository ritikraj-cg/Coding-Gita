# JavaScript Day 002 — Introduction to Variables and Datatypes

According to the given notes.

Question 1:

I will use const for the values that will never change and the let keyword for the age that will change.

Question 2:

The appropriate keyword to declare the score variable is let . The reason is that we reassigned the value of 80 to it.

Question 3:

We should use the keyword const to declare PI . The reason is that PI will never be changed or reassigned.

Question 4:

The var and let variables can be declared with no initial value. The default value is undefined until the assignment.

Question 5:

I will declare the studentName and schoolName with the const keyword since they hold constant values. The marks will be with let since it is a mutable value.

Question 6:

The var keyword is function-scoped and can be accessed outside the if block. The let keyword cannot be accessed outside the block.

Question 7:

The difference is that the var keyword can be re-declared in the same scope, but the let cannot.

Question 8

The same applies to var and let keywords; they can be assigned new values. On the other hand, the const variables cannot.

Question 9:

The result of x is 20 because the var keyword is function-scoped. However, y and z cannot be accessed since they are block-scoped variables.

Question 10:

The country variable must be initialized with some value. On the other hand, the city can be reassigned to another value, and the score cannot be declared again in the same scope.

Question 11

The var variable is hoisted and initialized with undefined value. The let variable is hoisted but not initialized, so it throws an error if accessed before declaration. The const variable also throws an error if accessed before declaration.

Question 12:

The code moves the declarations to the top of the scope. Therefore, the hoisted variables have undefined values, and the assigned variables have their values.

Question 13:

The whole numbers are integers and decimal numbers are float, but both are of type number. Text values are of type string, and boolean values are true and false.

Question 14

Undefined means that a variable has been declared, but it does not have a value. Null is different from undefined because it represents an empty value. When you pass typeof null , it will return an object.

Question 15:

Infinity and -Infinity are numbers in JavaScript. NaN is also a number, although it represents an invalid or undefined value. Scientific and engineering notations are valid ways to represent numbers, so they are of type number. BigInt is used to represent very large integers, so it is also a number.

Question 16:

In JavaScript, strings can be written with single quotes, double quotes, or backticks. The last option is used to write template literals.

Question 17:

Every Symbol() call returns a unique value. Therefore, these two variables are not equal.

Question 18:

The normal number type has limitations, so JavaScript has a BigInt type to hold extremely large integers. It is necessary to write n at the end of the number.

Question 19:

As discussed, Symbol() provides unique values. BigInt is used for integers that are too large. An uninitialized variable is undefined, and null is used for empty values.

Question 20:

The results are as follows:
undefined undefined
object null
number 42
string Hello
boolean true
symbol Symbol(key)
bigint 123n

Question 21:

The incorrect parts are the string, boolean, null, Symbol(), and BigInt value. The correct code should have the following parts:

Question 22:

Primitive types are the most basic data types. An object is a data type that is not primitive.