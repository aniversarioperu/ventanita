.PHONY: help migrations serve test coverage imports

help:
	@echo "  test migrations   to apply model migrations to TEST SQLITE db"
	@echo "  migrations   to apply model migrations"
	@echo "  serve        to start application in localhost"
	@echo "  test         to run unittests"
	@echo "  coverage     to estimate code coverage by the unittests"
	@echo "  imports      to import all available data into our database"

test_migrations:
	python ventanita/manage.py makemigrations --settings=ventanita.settings.testing
	python ventanita/manage.py migrate --settings=ventanita.settings.testing

migrations:
	python ventanita/manage.py makemigrations --settings=ventanita.settings.local
	python ventanita/manage.py migrate --settings=ventanita.settings.local

imports:
	python ventanita/manage.py import_redam --jsonfile=../data/redam.jl --settings=ventanita.settings.local

serve:
	python ventanita/manage.py runserver --settings=ventanita.settings.local

test:
	coverage run --source ventanita ventanita/manage.py test -v 2 \
	    core pages \
	    --settings=ventanita.settings.testing

coverage: test
	coverage report -m
	coverage html
