//Object Oriented Programming in JS
// JS is not a class based object oriented language

//creating Employee Object with properties
function EmployeeObject(firstName,lastName,age){
	this.firstName = firstName;
	this.lastName = lastName;
	this.age = age;
}

//adding a new method to EmployeeObject
EmployeeObject.prototype.getFullname = function(){
	return this.firstName +' '+this.lastName; 
}

//creating a new instanace of the EmployeeObject and passing values for properties
var personOne = new EmployeeObject("Jhon","Doe",45);

console.log(personOne.firstName);
console.log(personOne.lastName);
console.log(personOne.age);
console.log(personOne.getFullname());


console.log("-------------------------------------------------")
//JavaScript introduced the class keyword in ECMAScript 2015

class Animals{
	constructor(name,specie){
		this.name =name;
		this.specie = specie;
	}

	sing(){
		return `${this.name} can sing`
	}
}

var bingo = new Animals('Bingo','Hairy');
console.log('The name is '+bingo.name);
console.log(bingo.sing());

//inheritence

class Cats extends Animals{
	constructor(name,specie,color){
		super(name,specie);
		this.color = color;
	}
	whiskers(){
		return `${this.name} has ${this.color} color`
	}
}

var clara = new Cats('Clara','Fairy','indigo');

console.log(clara.name);
console.log(clara.whiskers());