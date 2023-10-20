# ReviewPub
ActivityPub, peer review platform.

## Setup instructions
1. `cd backend`
2. `python -m venv .venv && source .venv/bin/activate` (optional)
3. `pip install -r requirements.txt`
4. `python manage.py makemigrations` (optional)
5. `python manage.py migrate`
6. `python manage.py loaddictionaries`
7. `python manage.py runserver`
8. `python manage.py createsuperuser` (optional)
