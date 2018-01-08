from . import app
import datetime
from flask import render_template, request, jsonify, abort
from project.models import TmpLog, User
from project import db
import requests
import json
from colormap import rgb2hex


# insert temp in db
def insert_temp(temp):
    db.session.add(TmpLog(float(temp), datetime.datetime.now()))
    db.session.commit()


# get last readings
def tmp_last(row_number=50, f=10):
    readings = db.session.query(TmpLog).filter(TmpLog.temp_value > f).order_by(TmpLog.id.desc()).limit(row_number).all()
    return readings


# prepare array for chart representation
def chart_prep(data):
    temp_array = [['Time', 'C'], ]
    for item in data:
        __b__ = [item.temp_data.strftime('%H:%M'), item.temp_value]
        temp_array.append(__b__)
        # log print(temp_array)
    return temp_array


# PUT https://api.lifx.com/v1/lights/d073d500d1a6/state
def man_lamp(state, color, bright, duration):
    try:
        response = requests.put(
            url="https://api.lifx.com/v1/lights/d073d500d1a6/state",
            headers={
                "Authorization": app.config['LIFX'],
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "duration": duration,
                "power": state,
                "brightness": bright,
                "color": color
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return response.status_code


# loaf mainpage
@app.route('/', methods=['GET'])
def templog():
    last_readings_t = tmp_last(10, 10)
    temp_array = chart_prep(tmp_last())
    return render_template('index.html', array=temp_array, readings=last_readings_t)


# log temperature endpoint
@app.route("/api/temp", methods=['POST'])
def post_temp():
    if request.json['user_id'] != app.config['KEY']:
        abort(401)
    else:
        try:
            insert_temp(request.json['payload']['percent'])
        except:
            abort(400)
    return jsonify({'result': 'ok'})


# manage lamp
@app.route("/api/lamp", methods=['PUT'])
def lamp():
    try:
        # convert rgb to hex
        color = rgb2hex(int(request.args.get('r')), int(request.args.get('g')), int(request.args.get('b')), False)
        # get and normalise brightness
        bright = float(request.args.get('br'))*0.01
        sw = str(request.args.get('sw'))
        print(request)
    except:
        abort(400)
    if sw == 'true':
        state = "on"
    else: state = 'off'
    print(state,color,bright)
    result = man_lamp(state, color, bright, 1)
    return jsonify({'result': result})


@app.route("/api/user", methods=['POST'])
def insert_user(temp):
    db.session.add(User('w@gmail.com', '12345'))
    db.session.commit()



#TODO Test coverage
