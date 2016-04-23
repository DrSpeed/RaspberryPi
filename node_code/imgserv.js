//include http, fs and url module
var http = require('http'),
    fs = require('fs'),
    path = require('path'),
    url = require('url');

var imageDir = 'img/';
var nCols = 3;
var curCol = 0;
//create http server listening on port 80
http.createServer(function (req, res) {
    //use the url to parse the requested url and get the image name
    var query = url.parse(req.url,true).query;
    pic = query.image;
    //console.log("hit me");

    // Get the directory-------------------------
    if (typeof pic === 'undefined') {
       console.log("list images");
	getImages(imageDir, function (err, files) {
	    res.writeHead(200, {'Content-type':'text/html'});
	    res.write('<html>');
	    res.write('<body>');
   	    res.write('<table>');
	    for (var i=0; i<files.length; i++) {
		var thisFile = files[i];
		if (thisFile.indexOf("_th") > 0){
		    if (curCol == 0)
			res.write('<tr>');
		    res.write('<td>');
		    var bigFile = thisFile.replace("_th", "");
		    //console.log(bigFile);
		    var shortName = thisFile.replace("_th.jpg", "").replace("capture", "");
		    res.write('<a href="/?image=' + bigFile + '"><img src="/?image=' + thisFile + '"/><br>' + shortName);
		    res.write('</td>');

		    if (curCol ==  (nCols-1) ){
			res.write('</tr>');
			curCol = 0;
		    } else {
			curCol = curCol+1;
		    }
		}
	    }
	    res.write('</table>');
	    res.write('</body>');
	    res.write('</html>');
   	    res.end();

	});
    // Stream the image-----------------	
    } else {
        console.log("Reading dir");
	//read the image using fs and send the image content back in the response
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

}).listen(8000);
console.log("Server running at http://localhost:8000/");

//get the list of jpg files in the image dir
function getImages(imageDir, callback) {
    //console.log("get images at " + imageDir);
    var fileType = '.jpg',
	files = [], i;
    fs.readdir(imageDir, function (err, list) {
	for(i=0; i<list.length; i++) {
	    if(path.extname(list[i]) === fileType) {
                //console.log("image " + list[i]); 
		files.push(list[i]); //store the file name into the array files
	    }
	}
	callback(err, files);
    });
}
