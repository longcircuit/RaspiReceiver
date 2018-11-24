.PHONY: venv

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements/requirements.txt && pip install -e .
	
