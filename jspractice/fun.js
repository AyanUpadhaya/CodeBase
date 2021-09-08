//using object literals

var person = {
	firstName: 'Jhon',
	lastName : 'Constantine',
	age: 35,
	isHandSome : true,
	isFighter: true,
	email : 'Jhon@Constantine.com'
};
let x = 8
const result = x >10 ? 'Greater':'lower';

switch(result){
	case 'Greater':
	    console.log('It is greater than 10');
	    break;
	case 'lower':
	    console.log('It is lower case than 10');
	    break;
	default:
	    console.log('No case match');
	    break;
}