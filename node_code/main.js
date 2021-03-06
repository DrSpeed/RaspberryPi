// To run: sudo nodejs main.js

var http = require("http"),
    fs = require('fs'),
    path = require('path'),
    url = require('url');

imageDir = '/home/pi/node/img/';

// sync version
function walkSync(currentDirPath, callback) {

    var fs = require('fs'),
	path = require('path');

    var allFiles = new Array();

    fs.readdirSync(currentDirPath).forEach(function (name) {
	var filePath = path.join(currentDirPath, name);
	var stat = fs.statSync(filePath);
	if (stat.isFile()) {  // Not rescursive, ignore directories
	    var tnFile = {
		path: filePath,
		stat:  stat,
	    };
	    allFiles.push(tnFile);
	}
    });

    // works well
    allFiles = allFiles.sort(function(a, b) {
	return fs.statSync(a.path).mtime.getTime() -
            fs.statSync(b.path).mtime.getTime();
    });

    allFiles = allFiles.reverse();
    
    // call the callback
    for (i = 0; i < allFiles.length; i++) {
	var tnFile = allFiles[i];
	callback(tnFile.path, tnFile.stat);	
    }

}



http.createServer(function (req, res) {

    // Send the HTTP header
    // HTTP Status: 200 : OK
    // Content Type: text/plain

    
    
    var query = url.parse(req.url,true).query;
    pic = query.image;
    console.log("hit me");

    // Get the directory-------------------------
    if (typeof pic === 'undefined') {
	res.writeHead(200, {'Content-Type': 'text/html'});  

	res.write('<html>');
	res.write('<head>');
	res.write('<title>Raspberry Pi Camera</title>');
	res.write('<meta http-equiv=\"refresh\" content=\"300\">');
	res.write('<style>');
	res.write('table, th, td {border: 1px solid black;border-collapse:border-collapse: separate;border-spacing: 5px 5px;font-size: 90%; }');
	res.write(' body { font-family:Arial; } img { border-color: black; }');
	res.write('</style>');
	res.write('</head>');
	res.write('<body>');

	var thumbnail = '_tn';
	var ncols = 6;
	var curcol = 0;

	res.write('<table>');
	walkSync('/home/pi/node/img', function(filePath, stat) {
	    if (filePath.indexOf(thumbnail) > -1)
	    {
		if (curcol == 0)
		{
		    res.write('\n');
		    res.write('<TR>');
		}
		res.write('<td>');
		var lio = filePath.lastIndexOf('/');
   		var justFile = '?img=' + filePath.substring(lio + 1, filePath.length);
		res.write('<a href="http://');
		var server = req.headers.host.substring(0, req.headers.host.length-3);
		res.write(server + '/');
		bigFile = justFile.replace('_th', '');
   		res.write(bigFile);
		res.write('\">');
   		res.write('<img src=\"http://' + server + '/' + justFile + '\">');
      		res.write('</a>');
		res.write('<br>' + justFile.substring(12, justFile.length-7));
		res.write('</td>');
		res.write('\n');

		curcol = curcol+1;
		if (curcol == ncols){
		    res.write('\n');
		    res.write('</TR>');
		    res.write('\n');
		    curcol = 0;
		}
	    }
	});

	res.write('</table>');
	res.end('</body></html>');
    } else {
	console.log("trying to get file" + pic);
	// Stream file
	fs.readFile(imageDir + pic, function (err, content) {
	    if (err) {
		res.writeHead(400, {'Content-type':'text/html'})
		console.log(err);
		res.end("No such image");
	    } else {
		//specify the content type in the response will be an image
		res.writeHead(200,{'Content-type':'image/jpg'});
		res.end(content);
	    }
	});

    }
}).listen(90);  // PORT HERE

// Console will print the message
console.log('Server running at http://127.0.0.1:90/');
