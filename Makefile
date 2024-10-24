.PHONY: install
install:
	pip install -e ".[dev]"

.PHONY: format
format:
	tox -e format

.PHONY: lint
lint:
	tox -e lint

.PHONY: build
build:
	tox -e build

