VENV_PATH = .venv

.PHONY: venv
venv:
	python3 -m venv $(VENV_PATH)
	$(VENV_PATH)/bin/pip install -U pip setuptools
	$(VENV_PATH)/bin/pip install poetry
	$(VENV_PATH)/bin/poetry config virtualenvs.in-project true
	$(VENV_PATH)/bin/poetry config virtualenvs.options.always-copy true


.PHONY: install
install:
	. $(VENV_PATH)/bin/activate && poetry install --no-root


.PHONY: clean
clean:
	rm -rf $(VENV_PATH)
	[ -f poetry.lock ] && rm poetry.lock


.PHONY: info
info:
	$(VENV_PATH)/bin/poetry env info --path