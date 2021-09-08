//functional programming

//arrays of objects

const todos =[
	{
		id:1,
		text:'Take out trash',
		isCompleted: true
	},
	{
		id:2,
		text:'Meeting with boss',
		isCompleted: true
	},
	{
		id:3,
		text:'Dentist appointment',
		isCompleted: false
	}
];
console.log("My tasks today are:")

for(let todo of todos){
	console.log(todo.text);
}

console.log();

//forEach ,map, filter

console.log('Using forEach array method')
todos.forEach(function(todo){
	console.log(todo.text);
});

//using map

console.log("Using Map");

const todoText = todos.map(function(todo){
	return todo.text;
});

console.log(todoText.join(','));

console.log()

//using filter function

const todoCompleted = todos.filter(function(todo){
	return todo.isCompleted ===true;
}).map(function(todo){
	return todo.text;
});

console.log(todoCompleted)




