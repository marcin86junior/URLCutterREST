URLCutterREST
=============

Overview
--------

URLCutterREST is a web application for "long link shortner". 
Django/REST technology is used for serialization and management of data.
On "homepage" site you can: add data, check list, remove unused data.

Celery and Celery-beat have now 3 tasks:

	- remove never unused links (created 1 day ago or more) at 8 AM
	- remove used links (not used from 5 days or more) at 11 PM
	- remove unused links every 1min (TEST TASK/TURN IT OFF)

Requirements:
-------------

	Python 3.8-3.10
	Django 3.2-4.1
	Djangorestframework 3.13-3.14
	Celery 5.1.2
	Redis 3.5.3

Roadmap
-------

Version 0.8
- link generator is working
- list of links is working
- views that removes unused / used links working
- view that clean up database is working
- added model Link to admin
- app 0.8 is working on pythonanywhere

Version 0.9
- put code on github - OK
- 2nd run on docker / correct docker-entrypoint.sh - OK
- correct tests code (path changed) - OK
- correct text in page after removing links (httpresponse) - OK
- setup celery + redis + "test task every 1min" - OK
- add 3 celery tasks  1min / 8 AM / 23 PM - OK
- add to readme: remove test task and remove test view for production - OK

Version 1.0 (current)
- add docker-test-cover to docker-entrypoint (working) - OK 

Version 1.1
- add "add-custom-premium link" - OK
- BUG "add-custom-premium link" count +1 not working
- add premium-custom-link time off (none, 1 day, 7days, 30days) to model / serializer (30min-1h)
- put to celery tasks "premium time-off checker and removal code:
- add TemplateHTMLRenderer to REST

Version 1.2
- add Throttling-REST 'anon': '50/day', 'user': '1000/day'
https://www.django-rest-framework.org/api-guide/throttling/
- correct docker-compose.yml (dblite to postgers/ settings)

Docker:
-------

	Create new folder "URLCutterREST" and open it:
	git clone https://github.com/marcin86junior/URLCutterREST.git .

	"CRLF->LF" in \mysite\docker-entrypoint.sh (for Windows users)   

	If you want go for "production stage app" please remove development parts:
	in \mysite\mysite\settings.py -> remove test task "test_task_every_minute"
	in urls.py -> remove: path('link_premium_generator/), path('list/') and all path('remove_*)
	
	cd mysite\
	docker-compose up
	http://127.0.0.1:8000/

	Docker tests are included in "\mysite\docker-entrypoint.sh"

Local installation (working without celery-beat and 3 time tasks)
-------------

	Create new folder "URLCutterREST" and open it:
	git clone https://github.com/marcin86junior/URLCutterREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd mysite\
	python manage.py migrate
	python manage.py makemigrations
	python manage.py migrate
	python .\manage.py runserver
	http://127.0.0.1:8000/

	Test:
	python manage.py test
