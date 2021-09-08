// prompt - sync is Node js module

// Make sure you have Node and NPM installed
// Run npm install prompt-sync in the termina

//The code below creates a small number guessing game

const input = require('prompt-sync')({sigint:true});

//random number from 1-10

const numberToGuess = Math.floor(Math.random()*10)+1;

//this variable is used to determine if the app
//should continue prompting the user for input

let foundCorrectNumber = false;

while(!foundCorrectNumber){
	//get user input
	let guess = input('Guess a number from 1 to 10:');

	//conver the string input to a number

	guess = Number(guess)

	//compare the guess to the secret answer and let the user know

	if (guess==numberToGuess){
		console.log('Congrats you got it!');
		foundCorrectNumber=true;
	}
	if(guess>numberToGuess){
		console.log('Too high');
	}
	if (guess<numberToGuess){
		console.log('Too low');
	}
}
