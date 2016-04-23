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


console.log(times);
console.log();
console.log(new Date());
console.log('Sunset:' + times.sunset);

var now = new Date();
console.log('Now: ' + now);
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
