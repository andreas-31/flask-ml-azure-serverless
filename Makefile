setup:
	python3 -m venv ~/.azure-devops
	#source ~/.azure-devops/bin/activate # fails if sh is used as shell
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt --quiet

test:
	python -m pytest -vv -rP --disable-pytest-warnings

lint:
	pylint --disable=R,C,W1203,W0702 tests/load/*.py tests/unit/*.py *.py

load:
	./make_predict_azure_app.sh &&\
		sleep 15  &&\
		locust --conf=tests/load/locust.conf -f tests/load/locustfile.py

loadlocalhost:
	locust --conf=tests/load/locust.conf -f tests/load/locustfile.py --host "http://localhost:5000"

all: install lint test
