# this is refactored version for landing site
# origenal version will be deleted soon
# production result: https://ukrainecontentclub.com.ua/

site type: Landing

hosting: current hosted on Film.ua

tech stack:

	backend framework: Django(Wagtail)
	frontend: HTML+CSS
	DB: SQLite
	Other: Docker, NGINX, Ubuntu
-----------------
Server config (my deployment recommendation):

 Hosted on Linux server (Ubuntu)
- fresh version preffered
- minimal installation.
- python version 3.10 and up
- installed docker
- installed tmux (or any tool to avoid disconnection troubles)

# Admin panel for stuff users and superusers:

https://site.name.tld/admin # wagtail admin-panel

https://site.name.tld/django-admin  # Django admin-panel

Virtual env:
python3.9 -m venv venv
source venv/bin/activate

git pull
pip install "gunicorn==20.0.4"
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --settings=core.settings.dev
python manage.py collectstatic  --settings=core.settings.dev --no-input --clear
python manage.py update_index  --settings=core.settings.dev

gunicorn core.wsgi:application -b :8081  --workers=5   --timeout=190 --graceful-timeout=100 --log-level=DEBUG

Docker
docker-compose up -d --build  or  docker-compose up  --build
docker-compose exec web python manage.py createsuperuser --settings=core.settings.dev
or
docker-compose exec web python manage.py createsuperuser --settings=core.settings.production