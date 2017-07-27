venv:
	python3 -m virtualenv --no-site-packages venv

test:
	python -m unittest tests.unit.test_stormtrooper

develop:
	python setup.py develop
