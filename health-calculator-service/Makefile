.PHONY: run test

PORT=80
DEBUG=False

-include .env

init:
	pip install -r requirements.txt

run:
	python src/app.py

test:
	python -m unittest

docker-build:
	docker build -t health-calculator-service .

docker-run:
	docker run --rm -p ${PORT}:${PORT} -e PORT=${PORT} -e DEBUG=${DEBUG} health-calculator-service

docker-test:
	docker run --rm -it -p ${PORT}:${PORT} -e PORT=${PORT} -e DEBUG=${DEBUG} health-calculator-service -m unittest