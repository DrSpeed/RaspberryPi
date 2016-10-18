// Called by cron to take sunset pictures

var dateFormat = require('dateformat');
var SunCalc    = require('suncalc');
var sys        = require('sys')

// location of emeryville, ca on earth
lat = 37.8;
lon = -122.3;
paramTime = process.argv[2];

console.log('paramTime:' + paramTime);  // The cron supplied minute of capture

// get today's sunlight times for London
var times = SunCalc.getTimes(new Date(), lat, lon);

// get position of the sun (azimuth and altitude) at today's sunrise
var sunrisePos = SunCalc.getPosition(times.sunrise, lat, lon);

// get sunrise azimuth in degrees
var sunriseAzimuth = sunrisePos.azimuth * 180 / Math.PI;

//var aws_iot = "/home/pi/aws_iot/samples/linux/subscribe_publish_sample/subscribe_publish_sample -x 1";

// Calculate sunset (golden hour) end
var postSunset = new Date(times.sunset);
postSunset.setMinutes(times.sunset.getMinutes() + 30);
// Calculate pre-sunrise (morning golden hour)
var preSunrise = new Date(times.sunrise);
preSunrise.setMinutes(times.sunrise.getMinutes() - 30);

var now = new Date();
var file_time = dateFormat(now, "ddd_hh_MM_TT");
var img_dir = "/var/www/html/img/";
var img_fn    = "capture_" + file_time + ".jpg";
var img_tn_fn = "capture_" + file_time + "_th.jpg";
var img_file = img_dir + img_fn;
var tn_file  = img_dir + img_tn_fn;

function puts(error, stdout, stderr) { sys.puts(stdout) }

var onHour = (paramTime == 0);

// Always take a 15 minute picture if it's after morning and before
// postSunset
if ((paramTime % 15) == 0){  // sjw: should be 15
    // after sunrise and before the end of golden hour
    if ( (now >= preSunrise) && (now <= postSunset)){
	var exec = require('child_process').exec;
	
	// These commands have to by synchronous, the capture HAS to be done before the 
	var cmd1 = "/var/www/html/capture.sh " + img_file + " " + tn_file;
	var cmd2 = "/usr/bin/python /home/pi/python/timed_cap.py " + img_fn + " " + img_file;
	exec(cmd1 + "; " + cmd2 ,  puts);

	//exec(aws_iot, puts);  Too much $$
	
	// Plotly says 250 day, but fails after 25/day
	if (onHour){
	    exec("sudo /usr/bin/python /home/pi/plotly/add_shot.py");
	}
    } else {  // No shot
	if (onHour){
	var exec = require('child_process').exec;
	    exec("sudo /usr/bin/python /home/pi/plotly/no_shot.py");
	}
    }
}
else{ // Take any non-15 minute picture at sunset

    // Calculate the pre-sunset time 1/2 hour before sunset
    // Sunrise is not so interesting, we don't do 5 min pics
    var preSunset = new Date(times.sunset);
    preSunset.setMinutes(times.sunset.getMinutes() - 30);
    if ( (now >= preSunset) && (now <= postSunset)){
	var exec = require('child_process').exec;
	
	// These commands have to by synchronous
	var cmd1 = "/var/www/html/capture.sh " + img_file + " " + tn_file;
	var cmd2 = "/usr/bin/python /home/pi/python/timed_cap.py " + img_fn + " " + img_file;
	exec(cmd1 + "; " + cmd2 ,  puts);

	//exec(aws_iot, puts);  Too much $$
	// Plotly promises 250/day but complains after 25/day
	//exec("sudo /usr/bin/python /home/pi/plotly/add_shot.py");
    }
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
