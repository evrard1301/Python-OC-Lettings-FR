tests:
	pytest

cov:
	pytest --cov=.

cov_html:
	pytest --cov=. --cov-report=html

lint:
	flake8 .
