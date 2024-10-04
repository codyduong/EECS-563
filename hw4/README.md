# Homework 4 | EECS 563

---

The report for homework 4 can be found in [REPORT.md](./REPORT.md)

## Requirements

* `python 3.12^.0`
  * This is just the version of python I have, and haven't tested it on other versions

## Run

```sh
python TCP-server.py 6000
python TCP-client.py 127.0.0.1 6000
python UDP-server.py 6000
python UDP-client.py 127.0.0.1 6000
```


<!-- ## Tests

Test cases are written using [ `unittest` ](https://docs.python.org/3/library/unittest.html) for testing. The tests can be found in [ `./tests` ](tests).

Run tests with python tests/main.py -v -->

## Formatting
[`black`](https://github.com/psf/black) is used for formatting and code-styling.

```sh
black .
```