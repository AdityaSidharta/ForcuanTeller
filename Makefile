build:
	poetry install

load:
	export PYTHONPATH=${PYTHONPATH}; python -m forcuanteller.main.loader

transform:
	export PYTHONPATH=${PYTHONPATH}; python -m forcuanteller.main.transformer

reporter:
	export PYTHONPATH=${PYTHONPATH}; python -m forcuanteller.main.reporter

run: load transform reporter