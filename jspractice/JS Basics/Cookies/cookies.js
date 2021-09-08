//cookies

function createCookies(cookieName,value,daysToExpire){
	let date = new Date();
	date.setTime(date.getTime+(daysToExpire*24*60*60*1000));
	document.cookie = cookieName + "=" +value+"; exprires="+date.toGMTString();
}
function accessCookies(cookieName){
	let name = cookieName+"="

	let allArrayCookie = document.cookie.split(';');
	for(i=0;i<allArrayCookie.length;i++){
		var temp = allArrayCookie[i].trim();
		if (temp.indexOf(name)==0){
			return temp.substring(name.length,temp.length);
		}

	}
	return "";

}

function checkCookie(){
	var user = accessCookies('testCookie');
	if (user!=""){
		alert("Welcome back user");
	}
	else{
		user = prompt("Please enter your name");
		num = prompt("Please enter how many days you want name to be store?");

		if (user!="" && user!=null){
			createCookies('testCookie',user,num);
		}
	}
}
checkCookie()