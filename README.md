URLCutterREST
=============

Overview
--------

URLCutterREST is a web application for "long link shortner". 
Django/REST technology is used for serialization and management of data.
On "homepage" site you can: add data, check list, remove unused data.

Celery and Celery-beat have now 2 tasks:

	- remove never unused links (created 1 day ago or more) at 8 AM
	- remove used links (not used from 5 days or more) every 1h

Requirements:
-------------

	Python 3.8-3.10
	Django 3.2-4.1
	Djangorestframework 3.13-3.14
	Celery 5.1.2
	Redis 3.5.3


Roadmap
-------

Version 0.8 (current)
- link generator is working
- list of links is working
- views that removes unused / used links working
- view that clean up database is working
- added model Link to admin
- app 0.8 is working on pythonanywhere

Version 0.9
- correct "HTTP 405 Method Not Allowed" on "add-view" (importatnt)
- correct text after removing links (httpresponse)
- put code on github
- 2nd run on docker
- simplify randomize link (model/view)
- correct tests (path changed / new views)

Version 1.0
- add celery module (will work only with docker)
- remove "list view"

Version 1.1
- to correct from dblite to postgers in docker 
- add front page template
- more advanced test + covarage

Version 1.2
- add Throttling-REST 'anon': '50/day', 'user': '1000/day'
https://www.django-rest-framework.org/api-guide/throttling/

Issues
------

    - correct "HTTP 405 Method Not Allowed" on "add-view" -> 200 (important)
	- sometimes djano run get and run count (+1) (to be corrected)

Docker:
-------

	Create new folder "URLCutterREST" and open it:
	git clone https://github.com/marcin86junior/URLCutterREST.git .
	"CRLF->LF" in \mysite\docker-entrypoint.sh (for Windows users)   
	Please setup crontab in \mysite\mysite\settings.py -> now it's 8:00 / evry 1h (you can change to every minute)
	Run Doker Desktop in Windows.	
	cd mysite\
	docker-compose up
	http://127.0.0.1:8000/

	Docker tests:
	You can add to \mysite\docker-entrypoint.sh this code:
	echo "Test website"
	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report
	
	docker-compose up
	In terminal you will see coverage.

Testing:
--------

	python manage.py test
	coverage run --source='.' --omit='*migrations*,*init*,*wsgi*,*asgi*,*urls*,*manage*,*admin*,*apps*,*settings*,*test*,*seriali*' manage.py test
	coverage report (or) coverage html

Installation (working without celery-beat):
-------------

	Create new folder "URLCutterREST" and open it:
	git clone https://github.com/marcin86junior/URLCutterREST.git .
	python -m venv myvenv
	.\myvenv\Scripts\activate
	pip install -r requirements.txt
	cd mysite\
	python manage.py migrate
	python manage.py makemigrations
	python .\manage.py runserver
	http://127.0.0.1:8000/

	# probably we can run in new terminal celery / celery-beat somehow
	..........

	python manage.py test

