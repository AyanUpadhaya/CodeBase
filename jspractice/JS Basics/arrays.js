//two ways to create js arrays

var hobbies = ['guitar','books','programming'];


console.log('My hobbies are');

for (i=0;i<hobbies.length;i++){
	console.log(hobbies[i]);
}


console.log("==============================================");

//another way is to use constructor

students = new Array("Jhon","Ram","Benjamin","Ann", "Aaron", "Edwin", "Elizabeth");

// prototype for adding new properties or method

Array.prototype.displayItems = function(){
	for (i=0;i<this.length;i++){
		console.log(this[i]);
	}
}

// length property --> If you want to know the number of elements in an array, you can use the length property.
// prototype property --> If you want to add new properties and methods, you can use the prototype property.
// reverse method --> You can reverse the order of items in an array using a reverse method.
// sort method --> You can sort the items in an array using sort method.
// pop method --> You can remove the last item of an array using a pop method.
// shift method --> You can remove the first item of an array using shift method.
// push method --> You can add a value as the last item of the array.



students.reverse();
students.sort();
students.pop();
students.push('Laxman');

//displaying array items
students.displayItems();

