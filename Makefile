SERVICE=sandbox

start: stop
	@echo 'start ...'
	docker-compose up -d --build

stop:
	@echo 'stop ...'
	docker-compose stop
	docker-compose rm -f

test: start
	@echo 'lint ...'
	docker-compose run --rm ${SERVICE} pipenv run lint
	@echo 'test ...'
	docker-compose run --rm ${SERVICE} pipenv run test_small
	docker-compose run --rm ${SERVICE} pipenv run test_medium

test_docker: start
	@echo 'lint ...'
	docker-compose run --rm ${SERVICE} flake8 --max-line-length=120 --ignore=E402 src
	@echo 'test ...'
	docker-compose run --rm ${SERVICE} nosetests --nologcapture --attr size=Small src/tests
	docker-compose run --rm ${SERVICE} nosetests --nologcapture --attr size=Medium src/tests
