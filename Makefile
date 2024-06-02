install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

reinstall:
	pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

test:
	poetry run pytest