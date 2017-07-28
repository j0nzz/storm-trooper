venv:
	python3 -m virtualenv --no-site-packages venv

test:
	python -m unittest discover stormtrooper.tests

develop:
	python setup.py develop

run:
	python -m stormtrooper.stormtrooper ${ARGS}
