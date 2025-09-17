
## Пример сборки, запуска и тестов:

```console
foo@bar:~$ docker build --no-cache --squash -t python_2025_11 -f Dockerfile .
foo@bar:~$ docker run -v ~/PycharmProjects/python_2025_11:/src -it python_2025_11 /bin/bash
foo@bar:~$ uv run main.py
foo@bar:~$ uv run python -m pytest tests
foo@bar:~$ uv run pylint . --ignore .venv
```

