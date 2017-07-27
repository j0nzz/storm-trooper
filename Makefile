venv:
	python3 -m virtualenv --no-site-packages venv

test:
	python -m unittest discover tests.unit

develop:
	python setup.py develop

run:
	python -m stormtrooper.stormtrooper report -22.53482 -43.21828 10
