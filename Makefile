SHELL := /usr/bin/bash

setup:
	python3.7 -m venv ~/.azure-devops
	source ~/.azure-devops/bin/activate
	
install:
	source ~/.azure-devops/bin/activate
	pip install --upgrade pip &&\
		pip install -r requirements.txt --quiet

test:
	source ~/.azure-devops/bin/activate
	python -m pytest -vv -rP --disable-pytest-warnings

lint:
	source ~/.azure-devops/bin/activate
	pylint --disable=R,C,W1203,W0702 tests/load/*.py tests/unit/*.py *.py

load:
<<<<<<< Updated upstream
	./make_predict_azure_app.sh &&\
		sleep 15  &&\
		locust --conf=tests/load/locust.conf -f tests/load/locustfile.py
=======
	source ~/.azure-devops/bin/activate
	locust --conf=tests/load/locust.conf -f tests/load/locustfile.py
>>>>>>> Stashed changes

all: install lint test
