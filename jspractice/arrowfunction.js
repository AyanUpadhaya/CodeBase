//functions


function addNum(numOne = 1, numTwo = 2){
	console.log(numOne+numTwo);
}
addNum(5,3);

//arrow function

const divide = (numOne,numTwo) =>{
	return numOne/numTwo;
}
 

const multiply = (numOne,numTwo)=>numOne*numTwo;


// const totalMultiply = multiply(3,2)

console.log(multiply(3,2));

console.log(divide(8,4));