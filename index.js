var express = require('express');
var app = express();
var http = require('http').createServer(app);
var io = require('socket.io')(http);
var fs = require('fs');
var system = require('child_process');


var file = {
	save: function(name,text){
		fs.writeFile(name,text,e=>{
			if(e) console.log(e);
		});
	},
	read: function(name,callback){
		fs.readFile(name,(error,buffer)=>{
			if (error) console.log(error);
			else callback(buffer.toString());
		});
	}
}

const port = 80;
const path = __dirname+'/';

app.use(express.static(path+'site/'));
app.get(/.*/,function(request,response){
	response.sendFile(path+'site/');
});

http.listen(port,()=>{console.log('Serving Port: '+port)});

io.on('connection',function(socket){
	var name,s;
	socket.on('research',subject=>{
		file.save('done.txt','false')
		console.log('Researching: '+subject.split('\n')[0]);
		file.save('here.txt',subject);
		s = subject;
		system.exec('startpy.bat');
	});
	socket.on('done',()=>{
		file.read('done.txt',bool=>{
			if(bool == 'true'){
				file.read('here.txt',text=>{
					socket.emit('info',text);
				});
			}
		});
	});
});