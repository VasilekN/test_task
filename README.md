# Parse service
A Django-based web service that provides an API with endpoints to create pages, get pages by ID, and list pages with optional ordering.

## Installation
1. Clone the repository:
```
git clone https://github.com/VasilekN/test_task.git
cd test_task
```
2. Create and activate a virtual environment:
```
python -m venv env
source env/bin/activate # Linux/MacOS
env\Scripts\activate    # Windows
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Database and migrations
1. Configure Database Settings 
- Run MySQL with docker compose. You can use another database if you want. 
```
$ docker compose up -d
```
- Open the settings.py file in your project directory. Find the DATABASES dictionary.
- Check the database connection details, such as engine, name, user, password, host, and port.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Or 'postgresql', 'sqlite3', etc.
        'NAME': 'database',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
2. Apply migrations
```
python manage.py migrate
```
3. Create superuser
```
python manage.py createsuperuser
```
Enter your desired username and press enter.
```
Username: admin
```
You will then be prompted for your desired email address:
```
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```

4. Stop and remove the containers
```
$ docker compose down
```

## Run the server
```
python manage.py runserver
```
By default, the server will be available at:
http://127.0.0.1:8000

The Django admin site is activated by default. You can open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/.
Try logging in with the superuser account which you created. You should see the Django admin index page.

