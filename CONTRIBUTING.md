# Contributing

## Code Style

- [Black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort)  

  Black reformats the code and isort sorts imports so that all code looks the same across the codebase. Run Black and isort before opening a PR to make sure no linting issues fails the CI.

  ```bash
  make fix
  ```

- [mypy](https://github.com/python/mypy)  

  Mypy provides static typing which assists in finding bugs without having to run the program.

  I.e. with mypy this function is missing types and will therefore raise an error:

  ```python
  def hello(phrase):
      return hello
  ```

  A correct version of above function would be:

  ```python
  def hello(phrase: str) -> str:
      return hello
  ```

  Run mypy before opening a PR to make sure no type errors fails the CI.

  ```bash
  make type-check
  ```

- [pytest](https://github.com/pytest-dev/pytest)  

  Testing framework. All added tests must be green for CI to pass. Run all test suites with:

  ```bash
  make test
  ```

