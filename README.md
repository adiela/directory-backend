# Django API Boilerplate


Template project for creating django api backend


## Running the app locally

- Clone repoistory or click use this template to create a similar repository on your profile
- Create virtual environment in the project base directory using venv `virtual venv -p python3.6`
- Activate virtual environment `source venv/bin/activate`
- Install dependencies `pip install requirements.txt`
- Add environment variables for development settings (Use different settings for staging and production environments)
```
SECRET_KEY=<random string>
DJANGO_SETTINGS_MODULE="api.settings.development"
```
- Apply migrations `python manage.py migrate`
- Run server `python manage.py runserver`
