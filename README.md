# Coffee Website Django

A simple **Coffee Website** built using Django, showcasing coffee services, menu, contact details, and more.  
This project is structured and ready for local development.

---

## Features

- Home page with coffee menu overview  
- About Us and Contact Us pages  
- Reservation/service request page  
- Email integration using Gmail SMTP  
- Static and media file handling

---

## Technologies Used

- Python 3.x  
- Django 5.x  
- SQLite (default database)  
- HTML, CSS, JavaScript  

---

## Installation



##Create Virtual Environment
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate



###Install Dependencies
pip install -r requirements.txt


###Apply Migrations

python manage.py migrate
python manage.py createsuperuser  # optional



##Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.



###Project Structure

Coffee_website_django/
│
├── newproject/          # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── service/             # Django app
│   ├── models.py
│   ├── views.py
│   └── templates/
│
├── templates/           # Global templates
├── static/              # CSS, JS, images
├── media/               # Media files
├── manage.py
└── requirements.txt

###Configuration


SECRET_KEY: Set in settings.py or use environment variables for production

DEBUG: False for production

ALLOWED_HOSTS: Add your deployment URL

Email: Configure Gmail SMTP in settings.py






Author

Pragati Pal

###clone the repository
```bash
git clone https://github.com/pragatipal21/Coffee_website_django.git
cd Coffee_website_django
