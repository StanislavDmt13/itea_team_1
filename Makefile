BLACK=black --line-length 88 --target-version py310

.PHONY: server check format test

server:
	$(RUNNER) python manage.py runserver

check:
	$(RUNNER) flake8 .
	$(RUNNER) $(BLACK) --fast --check .
	$(RUNNER) isort --check-only .

format:
	$(RUNNER) $(BLACK) .
	$(RUNNER) isort .

test:
	$(RUNNER) python manage.py test