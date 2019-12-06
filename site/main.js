var socket = io();

function obj(id){
	return document.querySelector(id);
}

Node.prototype.on = function(a,b,c){
	this.addEventListener(a,b,c);
}


obj('button').on('click',function(){
	let data = obj('input').value;
	if(data) socket.emit('research',data+'\n'+(!obj('#chk').checked));
	cont = true;
	obj('div').innerHTML = '';
	obj('p').innerHTML = 'Researching'
	ttry();
});

obj('input').focus();

let cont;

function ttry(){
	if(cont) setTimeout(ttry,1000);
	socket.emit('done');
	obj('p').innerHTML += '.'
}

socket.on('info',text=>{
	cont = false;
	showResearch(text);
	obj('p').innerHTML = '';
});

function showResearch(text){
	console.log(text);
	obj('div').innerHTML = text.split('\n').join('<br>');
}