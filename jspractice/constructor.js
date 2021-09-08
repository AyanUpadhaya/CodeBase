// constructor function

function Person(firstName,lastName,age,dateOfBirth){
	this.firstName = firstName;
	this.lastName = lastName;
	this.age = age;
	this.dateOfBirth = new Date(dateOfBirth);
}

//adding method to Person using prototype

Person.prototype.getFullname = function(){
	return this.firstName+' '+this.lastName;
}

Person.prototype.getBirthYear = function(){
	return this.dateOfBirth.getFullYear();
}



//instantiate object

let jhon = new Person('Jhon','Doe',49,'10-28-1992');

console.log(jhon.getFullname());

console.log(jhon.getBirthYear());



//using classes

class Employee{
	constructor(fullName,salary){
		this.fullName = fullName;
		this.salary = salary;
	}

	getEmployeeInfo(){
		return `Name: ${this.fullName} and salary is ${this.salary}`;
	}
}

let eric = new Employee('Eric Hansen',20000);

console.log(eric.getEmployeeInfo());