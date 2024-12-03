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
	rm -rf dist/
	tox -e build

.PHONY: publish-pip
publish-pip:
	tox -e publish

.PHONY: publish-conda
publish-conda:
	cd ./conda-recipe && conda build . && conda build purge

