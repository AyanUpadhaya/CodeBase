//conditional programming

let x = 5;
let y = 10;
if (x==7 && y==10){
	console.log('x is greater than six');
}else{
	console.log('None or one of the condition does not match');
}

//ternary operator

const color = x>=6 ? 'red':'blue';

//switch case

switch(color){
	case 'red':
		console.log("The color is red");
		break;

	case 'blue':
		console.log("The color is blue");
		break;

	default:
		console.log("No color match");
		break;

}