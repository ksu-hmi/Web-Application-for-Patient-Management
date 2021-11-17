from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.doctor import Doctors, Doctor
from package.appointment import Appointments, Appointment

# Added new
from package.insurance import Insurances, Insurance
from package.billing import Billings, Billing
from package.pcheckin import PCheckins, PCheckin

from package.common import Common
import json


with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:id>')
api.add_resource(Common, '/common')


# Add new
api.add_resource(Insurances, '/insurance')
api.add_resource(Insurance, '/insurance/<int:id>')
api.add_resource(Billings, '/billing')
api.add_resource(Billing, '/billing/<int:id>')
api.add_resource(PCheckins, '/pcheckin')
api.add_resource(PCheckin, '/pcheckin/<int:id>')

# Routes

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])
