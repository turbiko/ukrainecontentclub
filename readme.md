#this is refactored version for landing site
# original: git: https://github.com/turbiko/ucc_w
# Сайт: https://ukrainecontentclub.com.ua/

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
