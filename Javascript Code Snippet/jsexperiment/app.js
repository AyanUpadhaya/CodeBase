

// btn.addEventListener('click',(e)=>{
// 	e.preventDefault();//to prevent default behave
// 	document.querySelector('.submit_form').style.background="#a4a6a6";
// 	document.querySelector('body').style.background = "#2f3232";
// 	document.querySelector('h2').style.fontFamily = "Ubuntu";
// 	document.querySelector('h2').style.color = "#ffffff";

// });

const formElement = document.querySelector('.submit_form');
const user = document.querySelector('#username');
const password = document.querySelector('#password');
const btn = document.querySelector('button');
const msg = document.querySelector('.msg');
const infoList = document.querySelector('ul');

formElement.addEventListener('submit',validate);

function validate(e){
	e.preventDefault();
	if (user.value ==='' || password.value ===''){
		msg.innerHTML = "Please Enter Username and Password";
		setTimeout(()=>msg.remove(),3000);
	}else{

		const li = document.createElement('li');
		li.appendChild(document.createTextNode(`${user.value}: ${password.value}`));

		infoList.appendChild(li);

		//clear fields
		user.value = '';
		password.value ='';


	}
}
