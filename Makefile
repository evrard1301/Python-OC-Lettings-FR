unit_tests:
	pytest

cov:
	pytest --cov=.

cov_html:
	pytest --cov=. --cov-report=html

lint:
	flake8 .

build_docker_image:
	docker build . -t oc_lettings

run_docker_image:
	docker run -dp 8000:8000 oc_lettings
