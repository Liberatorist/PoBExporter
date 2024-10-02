## How set this up

To install all required dependencies run

```
python3 -m venv .venv
source .venv/bin/activate
poetry install
```

Download all the required data by running

```
python3 PoBExporter/_fetch.py
```

## How upload this to pypi

After setting this up, change the version in setup.py and run

```
python3 -m build
python3 -m twine upload dist/*
```

and enter pypi api-key when prompted
