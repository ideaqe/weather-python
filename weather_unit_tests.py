from webtest import TestApp
import weather_api
import json

app = TestApp(weather_api.app)


def test_get_weather():
    assert json.loads(app.get('/weather/1').body)[0]['temperature'] == "60"


def test_post_weather():
    assert app.post_json('/weather/', {'temperature': '675', 'observation_id': '9',
                                       'observation_time': '2016-11-20T04:00:00+00:00', 'station_id': '15',
                                       'humidity': '25.76', 'precipitation': '0'}).status == "200 OK"
    assert json.loads(app.get('/weather/15').body)[0]['temperature'] == "675"
