unit_tests:
	pytest

cov:
	pytest --cov=.

cov_html:
	pytest --cov=. --cov-report=html

lint:
	flake8 .

lint_html:
	flake8 . --format=html --htmldir=flake_report

build_docker_image:
	docker build . -t bog13/lettings

run_docker_image:
	docker run -dp 8000:8000 bog13/lettings

push_docker_image: build_docker_image
	docker push bog13/lettings

