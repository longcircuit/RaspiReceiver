.PHONY: venv

venv:
	python3.6 -m venv venv
	. venv/bin/activate && pip install -r requirements/requirements.txt
