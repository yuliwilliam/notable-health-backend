# Notable Health Backend API

This is a backend API implementation of

## Environment Setup

```
$ pip install -r requirements.txt
```

## API Usage

```
$ python3 app.py
```

By default, the API will listen on localhost port 5000 (i.e. http://localhost:5000).

## API Routes

### /api/doctors

- method: get  
- parameters: n/a  
- description: return a list of all doctors

### /api/appointments

- method: get  
- parameters:
  - `doctor id`: id of the doctor
  - `time`: timestamp of the desired date
- description: return a list of all appointments for a particular doctor and particular day

### /api/delete-appointment

- method: delete  
- request body:
  - `appointment id`: id of the appointment
- description: delete an existing appointment from a doctor's calendar

### /api/book-appointment
- method: post  
- request body:
  - `first name`: first name of the patient
  - `last name`: last name of the patient
  - `time`: timestamp of the appointment, appointments can only start at 15 minute intervals
  - `kind`: kind of the appointment, New Patient or Follow-up
  - `doctor id`: id of the appointment doctor
- description: add a new appointment to a doctor's calendar, return appointment details