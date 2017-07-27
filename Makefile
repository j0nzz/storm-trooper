venv:
	python3 -m virtualenv --no-site-packages venv

test:
	python -m unittest discover tests.unit

develop:
	python setup.py develop
