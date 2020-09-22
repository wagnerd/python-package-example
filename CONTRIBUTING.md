# Contributing to the package

## Development Environment

First create a virtual environment:
```bash
python -m venv venv
```

You can simply install the package in editable mode from inside the venv:

```bash
pip install -e .
```

This will also install the required packages listed in [setup.cfg](setup.cfg) as `install_requires`.

But consider that changes to the setup files are only applied if you reinstall the package.

If you want to create the package run:

```bash
python setup.py sdist
```

In order to run all the unit tests, pylint and coverage inside the package, do:

Install all necessary packages for testing inside your environment as a prerequisite:

```bash
pip install -r requirements-test.txt
```

Now run the tests, pylint and coverage with one command:

```bash
pytest --pylint --cov=src .
```

You can create the coverage report with:
```bash
coverage html
```

There is also an example for mypy, which can be run with:
```bash
mypy src tests
```
