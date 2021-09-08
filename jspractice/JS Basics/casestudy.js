let playerStatus='first'

switch(playerStatus){
	case 'first':
		console.log("First position");
		break;
	case 'second':
		console.log('Second Position');
		break;
	
	case 'third':
		console.log('Third Position');
		break;
	default:
		console.log('No position');
		break;
}

var mylist=['Rajib','Shajid','Shemon'];

for(var i=0;i<mylist.length;i++){
	console.log(mylist[i]);

}

console.log("total number of entries in list: ",mylist.length);
