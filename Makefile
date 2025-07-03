.PHONY: build test clean release pypi-check

build:
	python -m build

test: build
	python -m venv testenv
	. testenv/bin/activate && pip install dist/*.whl && dicom-maker --help

clean:
	rm -rf dist build *.egg-info testenv

release: clean build pypi-check
	twine upload dist/*

pypi-check:
	twine check dist/*
