.PHONY: dev install lint format fix type test pre-commit docker build run compose-up compose-down migrate makemigrations shell superuser

PYTHON := python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

dev:
	$(PYTHON) manage.py runserver 0.0.0.0:8000

lint:
	ruff check .

format:
	black .
	ruff format .

fix:
	ruff check --fix .
	black .

type:
	mypy .

test:
	pytest -q

pre-commit:
	$(MAKE) format lint type test

migrate:
	$(PYTHON) manage.py migrate

makemigrations:
	$(PYTHON) manage.py makemigrations

shell:
	$(PYTHON) manage.py shell

superuser:
	$(PYTHON) manage.py createsuperuser

docker:
	docker build -t stability-monitor .

build: docker

run:
	docker run --env-file .env -p 8000:8000 stability-monitor

compose-up:
	docker compose up --build -d

# Собрать mock-сервер и запустить 30 контейнеров
mockservers:
	docker build -t stability-monitor-mock ./mock_servers
	bash ./mock_servers/start_multiple.sh

# Остановить все mock-серверы (по имени)
stop-mockservers:
	-docker stop $$(docker ps -q --filter "name=mock_server_")

compose-down:
	docker compose down
