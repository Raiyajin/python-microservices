-include .env
.PHONY: init run test build

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m unittest

build:
	docker build -t health-calculator .
