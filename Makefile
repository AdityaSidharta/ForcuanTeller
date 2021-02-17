build:
	poetry install

run:
	export PYTHONPATH=${PYTHONPATH}; python -m forcuanteller.main.main