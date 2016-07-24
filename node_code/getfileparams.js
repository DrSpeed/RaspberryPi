// usage  nodejs getfileparams.js <url> <localfilename>

var http = require('http');
var fs = require('fs');

var PARAM_0 = 2;
var PARAM_1 = 3

// 
var file_url    = process.argv[PARAM_0];
var output_file = process.argv[PARAM_1];

var file = fs.createWriteStream(output_file);
var request = http.get(file_url, function(response) {
    console.log("Writing to file " + output_file);
    response.pipe(file);
});



