// JavaScript Object literals

var person = {
	firstName:"Jhon",
	lastName: "Doe",
	age:45,
	isDeveloper: true,
	sayHello:function(){
		console.log("Hello world");
	}
}

console.log(person.firstName+' '+person.lastName);
console.log(person.isDeveloper);
person.sayHello();


var employee =  {
	firstName : "Ryan",
	lastName  : "Dhal" 
}
// change value
// employee['firstName'] = 'Ayan';

console.log(employee.firstName);