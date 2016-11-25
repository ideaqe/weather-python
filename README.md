# weather API
This is a simple web application that uses [bottle](http://bottlepy.org/docs/dev/index.html) to exposes the following endpoints


|API|Method|Example Request|Example Response|
|---|---|---|---|
|/weather/\<stations_id\>|GET|_**curl**_ http://localhost:8080/weather/7 |```
[{
	"temperature": "68",
	"observation_id": "4",
	"observation_time": "2016-11-20T04:15:00+00:00",
	"station_id": "7",
	"humidity": "26.7",
	"precipitation": "5.31"
}, {
	"temperature": "68",
	"observation_id": "9",
	"observation_time": "2016-11-20T04:15:00+00:00",
	"station_id": "7",
	"humidity": "26.7",
	"precipitation": "5.31"
}]
```|
|/weather/\<stations_id\>|GET|_**curl**_ http://localhost:8080/weather/7/4 |```
[{
	"temperature": "68",
	"observation_id": "4",
	"observation_time": "2016-11-20T04:15:00+00:00",
	"station_id": "7",
	"humidity": "26.7",
	"precipitation": "5.31"
}]
```|
|/weather|POST|_**curl**_ -X POST -d '{"temperature": "65", "observation_id": "9", "observation_time": "2016-11-20T04:00:00+00:00", "station_id": "8", "humidity": "25.76", "precipitation": "0"}' http://localhost:8080/weather -H "Content-Type: application/json" |```
[...{"temperature": "65","observation_id": "9","observation_time": "2016-11-20T04:00:00+00:00","station_id": "8","humidity": "25.76","precipitation": "0"}]
```|

------------------------------

## Running the application

The application runs on port `8080` by default.
start the application using
````
$ python weather_api.py
````

------------------------------

## Running tests
Running tests requires installing WebTest and nose. The details are on the [webtest homepage](http://docs.pylonsproject.org/projects/webtest/en/latest/)
and [nose homepage](https://nose.readthedocs.io/en/latest/)
### installation
````
$ pip install webtest
$ pip install nose
````

The tests can be run using

````
$nosetests
````
--------------------------------
## Sample Data
The data used in the application is located in data.csv. The sample is as below

|observation_id|station_id|temperature|humidity|precipitation|observation_time|
|---|---|---|---|---|---|
|1|1|60|37.78|5.27|2016-11-20T04:00:00+00:00|
