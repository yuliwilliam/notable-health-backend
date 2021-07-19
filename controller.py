import json
import uuid

from flask import request
from flask import jsonify
from datetime import datetime

from utils import initialize_logger

logger = initialize_logger('controller.py')


def load_doctors_data():
    return json.load(open('./doctors.json', ))


def load_appointments_data():
    return json.load(open('./appointments.json', ))


def update_doctors_data(doctors):
    with open('./doctors.json', 'w') as f:
        json.dump(doctors, f)


def update_appointments_data(appointments):
    with open('./appointments.json', 'w') as f:
        json.dump(appointments, f)


def get_doctors():
    return jsonify(load_doctors_data()), 200


def get_appointments():
    body = request.args
    if any(key not in body for key in ['doctor id', 'time']):
        return 'invalid request, missing data', 422

    doctor_id, time = body.get('doctor id'), body.get('time')

    if doctor_id not in [doctor['id'] for doctor in load_doctors_data()]:
        return 'invalid doctor id', 422

    result_appointments = []
    target_date = datetime.fromtimestamp(float(time)).date()
    for appointment in load_appointments_data():
        curr_appointment_date = datetime.fromtimestamp(float(appointment['time'])).date()
        if target_date == curr_appointment_date:
            result_appointments.append(appointment)
    return jsonify(result_appointments), 200


def delete_appointment():
    body = request.form
    if 'appointment id' not in body:
        return 'invalid request, missing appointment id', 422
    appointments = load_appointments_data()
    remaining_appointments = [appointment for appointment in appointments if
                              appointment['id'] != body.get('appointment id')]
    if len(appointments) != len(remaining_appointments):
        update_appointments_data(remaining_appointments)
        return 'deleted', 200
    return 'appointment not found', 200


def book_appointment():
    body = request.form
    if any(key not in body for key in ['first name', 'last name', 'time', 'kind', 'doctor id']):
        return 'invalid appointment, missing data', 422

    first_name, last_name, time, kind, doctor_id = body.get('first name'), body.get('last name'), body.get(
        'time'), body.get('kind'), body.get('doctor id')

    if kind not in ['New Patient', 'Follow-up']:
        return 'invalid appointment kind', 422
    if doctor_id not in [doctor['id'] for doctor in load_doctors_data()]:
        return 'invalid doctor id', 422

    time_object = datetime.fromtimestamp(float(time))
    if time_object.minute % 15 != 0 or time_object.second != 0 or time_object.microsecond != 0:
        return 'invalid time', 422

    new_appointment = {
        'id': str(uuid.uuid4()),
        "doctor id": doctor_id,
        "first Name": first_name,
        "last Name": last_name,
        "time": time,
        "kind": kind
    }
    appointments = load_appointments_data()
    appointments.append(new_appointment)
    update_appointments_data(appointments)
    return new_appointment, 200
