// Called by cron to take sunset pictures

var SunCalc = require('suncalc');

// location of emeryville, ca on earth
lat = 37.8;
lon = -122.3;

// get today's sunlight times for London
var times = SunCalc.getTimes(new Date(), lat, lon);

// format sunrise time from the Date object
var sunriseStr = times.sunrise.getHours() + ':' + times.sunrise.getMinutes();

// get position of the sun (azimuth and altitude) at today's sunrise
var sunrisePos = SunCalc.getPosition(times.sunrise, lat, lon);

// get sunrise azimuth in degrees
var sunriseAzimuth = sunrisePos.azimuth * 180 / Math.PI;


//console.log(times);
//console.log();
//console.log(new Date());


var now = new Date();
console.log('Now: ' + now);

var preSunset = new Date(times.sunset);
preSunset.setMinutes(times.sunset.getMinutes() - 30);
console.log('pre sunset: ' + preSunset);

console.log('Sunset:' + times.sunset);

var postSunset = new Date(times.sunset);
postSunset.setMinutes(times.sunset.getMinutes() + 30);
console.log('post sunset: ' + postSunset);

if ( (now > preSunset) && (now < postSunset)){
    console.log('Capturing sunset image.');
    //  ---------------
    var sys = require('sys')

    var exec = require('child_process').exec;

    function puts(error, stdout, stderr) { sys.puts(stdout) }

    exec("/var/www/html/capture.sh", puts);
    // --------------
} else {
    console.log('Not sunset, no image');
}


if ( now < times.sunset){
    console.log('daytime');

} else {
    console.log('nighttime');
}

if ( now < times.sunrise){
    console.log('pre dawn');

} else {
    console.log('after dawn');
}

if ( now < times.solarNoon){
    console.log('pre solar noon');

} else {
    console.log('after solar noon');
}
