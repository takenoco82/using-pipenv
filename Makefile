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
