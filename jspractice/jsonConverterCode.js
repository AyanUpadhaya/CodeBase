//multiple practice

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

//convert to json 

const todoJSON = JSON.stringify(todos)

console.log(todoJSON);