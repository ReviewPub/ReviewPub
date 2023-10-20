# ReviewPub

ActivityPub, peer review platform.

## How to set up

1. `python -m venv venv && source venv/bin/activate`(optional)
2. `cd backend`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py loaddata review_pub/fixtures/review_pub/*`
6. `python manage.py runserver`
7. `python manage.py createsuperuser`(optional)
