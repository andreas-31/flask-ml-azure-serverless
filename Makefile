setup:
	python3 -m venv ~/.azure-devops
	source ~/.azure-devops/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint --disable=R,C,W1203,W0702 tests/load/*.py tests/unit/*.py *.py
	# R refactoring related checks
	# C convention related checks
	# W1203: logging-fstring-interpolation
	#   Use %s formatting in logging functions
	#   Used when a logging statement has a call form of "logging.<logging method>(f"...")"
	# W0702: No exception type(s) specified (bare-except)

load:
	locust --conf=tests/load/locust.conf -f tests/load/locustfile.py

all: install lint test
