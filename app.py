from flask import Flask
from utils import initialize_logger

import controller

app = Flask(__name__)
logger = initialize_logger('api.py')


@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    return controller.get_doctors()


@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    return controller.get_appointments()


@app.route('/api/delete-appointment', methods=['DELETE'])
def delete_appointment():
    return controller.delete_appointment()


@app.route('/api/book-appointment', methods=['POST'])
def book_appointment():
    return controller.book_appointment()


if __name__ == '__main__':
    logger.info('started api on port 5000')
    app.run(host='0.0.0.0', port=5000)
