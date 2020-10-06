# Contributing to the package

## Development Environment

First create a virtual environment:

```bash
python -m venv venv
```

If the venv is not activated automatically, run:

```bash
venv\Scripts\activate
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

This project uses tox to run different environments:

* testenv:
  * pytest
  * pylint
  * coverage
  * mypy

* testenv:doc:
  * Sphinx

So in order to run the test simply install tox in your venv:

```bash
pip install tox
```

After that just run
```bash
tox
```

Look at the [tox.ini](tox.ini) file at the [testenv] section if you want to know what
is executed inside the tox environment and which python versions are tested.

The example output for a successfull run below:
```bash
GLOB sdist-make: F:\Github\public\python-package-example\setup.py
py3 inst-nodeps: F:\Github\public\python-package-example\.tox\.tmp\package\1\python-package-example-0.1.0.zip
py3 installed: astroid==2.4.2,atomicwrites==1.4.0,attrs==20.2.0,colorama==0.4.3,coverage==5.3,importlib-metadata==1.7.0,iniconfig==1.0.1,isort==5.5.3,lazy-object-proxy==1.4.3,mccabe==0.6.1,more-itertools==8.5.0,mypy==0.782,mypy-extensions==0.4.3,packaging==20.4,pluggy==0.13.1,py==1.9.0,pylint==2.6.0,pyparsing==2.4.7,pytest==6.0.2,pytest-cov==2.10.1,pytest-pylint==0.17.0,python-package-example==0.1.0,six==1.15.0,toml==0.10.1,typed-ast==1.4.1,typing-extensions==3.7.4.3,wrapt==1.12.1,zipp==3.2.0 
py3 run-test-pre: PYTHONHASHSEED='654'
py3 run-test: commands[0] | pytest --pylint --cov=src .
======================================================================== test session starts ========================================================================
platform win32 -- Python 3.7.4, pytest-6.0.2, py-1.9.0, pluggy-0.13.1 -- f:\github\public\python-package-example\.tox\py3\scripts\python.exe
cachedir: .tox\py3\.pytest_cache
rootdir: F:\Github\public\python-package-example, configfile: pytest.ini
plugins: cov-2.10.1, pylint-0.17.0
collected 7 items
--------------------------------------------------------------------------------
Linting files
...
--------------------------------------------------------------------------------

setup.py::F:\Github\public\python-package-example\setup.py::PYLINT SKIPPED
src/module1/__init__.py::F:\Github\public\python-package-example\src\module1\__init__.py::PYLINT SKIPPED
src/module1/module1_entry_points.py::F:\Github\public\python-package-example\src\module1\module1_entry_points.py::PYLINT PASSED
src/module1/mypy_examples.py::F:\Github\public\python-package-example\src\module1\mypy_examples.py::PYLINT PASSED
tests/test_unittests.py::F:\Github\public\python-package-example\tests\test_unittests.py::PYLINT PASSED
tests/test_unittests.py::test_unittest_one This is test_unittest_one
PASSED
tests/test_unittests.py::test_unittest_tow This is test_unittest_tow
PASSED

----------- coverage: platform win32, python 3.7.4-final-0 -----------
Name                                  Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------
src\module1\__init__.py                   0      0      0      0   100%
src\module1\module1_entry_points.py      11     11      2      0     0%
src\module1\mypy_examples.py              2      2      0      0     0%
-----------------------------------------------------------------------
TOTAL                                    13     13      2      0     0%


=================================================================== 5 passed, 2 skipped in 0.39s ==================================================================== 
py3 run-test: commands[1] | coverage html
py3 run-test: commands[2] | mypy src tests
Success: no issues found in 4 source files
______________________________________________________________________________ summary ______________________________________________________________________________ 
  py3: commands succeeded
  congratulations :)
```

For the creation of the documentation we use the tox section [testenv:doc] which can simply be run with

```bash
tox -e doc
```

This will create a folder **.tox\doc_out** which contains the 
created documentation and can be exported.