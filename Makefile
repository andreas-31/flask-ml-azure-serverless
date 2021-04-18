setup:
	python3 -m venv ~/.azure-devops
	source ~/.azure-devops/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt --quiet

test:
	python -m pytest -vv -rP --disable-pytest-warnings

lint:
	pylint --disable=R,C,W1203,W0702 tests/load/*.py tests/unit/*.py *.py

load:
	locust --conf=tests/load/locust.conf -f tests/load/locustfile.py

all: install lint test
