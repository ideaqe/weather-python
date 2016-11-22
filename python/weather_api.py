import csv
import json
import os
import bottle

from bottle import get, post, run, response, request,abort

weather_data = []
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
app = bottle.app()


@get('/weather/<stationid>')
@get('/weather/<stationid>/')
def get_weather(stationid):
    response.content_type = "text/JSON"
    station_data = []
    if not weather_data:
        init_data()
    for observation in weather_data:
        if observation['station_id'] == stationid:
            station_data.append(observation)
    return json.dumps(station_data, indent=4)


@post('/weather')
@post('/weather/')
def post_weather():
    weather_data.append(request.json)
    return json.dumps(weather_data,indent=4)


def init_data():
    global weather_data
    with open(os.path.join(__location__, 'data.csv'),'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        out = json.dumps([row for row in reader])
    weather_data = json.loads(out)

if __name__ == '__main__':
    init_data()
    app.run(host='localhost', port=8080, debug=True)
