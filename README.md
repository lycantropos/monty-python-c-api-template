{{project}}
{{"=" * project|length}}

[![](https://github.com/{{github_login}}/{{project}}/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/{{github_login}}/{{project}}/actions/workflows/ci.yml "Github Actions")
[![](https://codecov.io/gh/{{github_login}}/{{project}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{github_login}}/{{project}} "Codecov")
[![](https://img.shields.io/github/license/{{github_login}}/{{project}}.svg)](https://github.com/{{github_login}}/{{project}}/blob/master/LICENSE "License")
[![](https://badge.fury.io/py/{{project.replace("_", "-")}}.svg)](https://badge.fury.io/py/{{project.replace("_", "-")}} "PyPI")

In what follows `python` is an alias for `python{{min_python_version.split('.')[:2]|join('.')}}` or `pypy{{min_python_version.split('.')[:2]|join('.')}}`
or any later version (`python{{min_python_version.split('.')[0]}}.{{min_python_version.split('.')[1]|int + 1}}`, `pypy{{min_python_version.split('.')[0]}}.{{min_python_version.split('.')[1]|int + 1}}` and so on).

Installation
------------

Install the latest `pip` & `setuptools` packages versions
```bash
python -m pip install --upgrade pip setuptools
```

### User

Download and install the latest stable version from `PyPI` repository
```bash
python -m pip install --upgrade {{project}}
```

### Developer

Download the latest version from `GitHub` repository
```bash
git clone https://github.com/{{github_login}}/{{project}}.git
cd {{project}}
```

Install
```bash
python setup.py install
```

Development
-----------

### Bumping version

#### Preparation

Install
[bump2version](https://github.com/c4urself/bump2version#installation).

#### Pre-release

Choose which version number category to bump following [semver
specification](http://semver.org/).

Test bumping version
```bash
bump2version --dry-run --verbose $CATEGORY
```

where `$CATEGORY` is the target version number category name, possible
values are `patch`/`minor`/`major`.

Bump version
```bash
bump2version --verbose $CATEGORY
```

This will set version to `major.minor.patch-alpha`. 

#### Release

Test bumping version
```bash
bump2version --dry-run --verbose release
```

Bump version
```bash
bump2version --verbose release
```

This will set version to `major.minor.patch`.

### Running tests

Install dependencies
```bash
python -m pip install -r requirements-tests.txt
```

Plain
```bash
pytest
```

Inside `Docker` container:
- with `CPython`
  ```bash
  docker-compose --file docker-compose.cpython.yml up
  ```
- with `PyPy`
  ```bash
  docker-compose --file docker-compose.pypy.yml up
  ```

`Bash` script:
- with `CPython`
  ```bash
  ./run-tests.sh
  ```
  or
  ```bash
  ./run-tests.sh cpython
  ```

- with `PyPy`
  ```bash
  ./run-tests.sh pypy
  ```

`PowerShell` script:
- with `CPython`
  ```powershell
  .\run-tests.ps1
  ```
  or
  ```powershell
  .\run-tests.ps1 cpython
  ```
- with `PyPy`
  ```powershell
  .\run-tests.ps1 pypy
  ```
