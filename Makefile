.PHONY: flake
flake:
	docker-compose run --rm worker flake8 .
