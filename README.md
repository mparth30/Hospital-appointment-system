# Hospital Appointment System (Django)

## Features
- User roles: Patient, Doctor, Admin
- Patients can book appointments with doctors
- Doctors can view & manage appointments
- Admin can manage users and doctors
- Simple dashboard with counts

## Quick start
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
