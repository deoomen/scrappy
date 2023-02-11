# Scrappy

**Scrappy** is a simple Python script for my personal use that aggregates other Python scripts and can run them one by one.

The initial aim is to prepare one common environment under many different web scraping scripts.

## Installation

### Docker

```sh
docker compose up
```

### Python environment

```sh
pip install --no-cache-dir -r requirements.txt -r tools/requirements.txt -r scripts/requirements.txt
```

## Usage

```sh
python scrappy.py [SCRIPT_NAME]...
```

### Example usage

Run all scripts:

```sh
python scrappy.py
```

Run single script:

```sh
python scrappy.py Script1
```

Run multiple selected scripts:

```sh
python scrappy.py Script1 Script2 Script3 ...
```

## Custom additional scripts

The scraping scripts should be placed in folder `app/scripts`. Each script must be a class that extends the base class `ScrapMe` and implement `scrap` method.

```py
# app/ScrapMe/MyScrapScriptClass.py

from tools.ScrapMe import ScrapMe

class MyScrapScriptClass(ScrapMe):

    def scrap(self) -> None:
        print('scraping time...')
```

The base class `ScrapMe` uses the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library and contains a `_loadPage` method with which you can download the content of a web page. `_loadPage` method returns a `BeautifulSoup` object.

In `app/scripts` directory you can find three examples of usage:

- `app/scripts/Sample1.py` - just "Hello world"
- `app/scripts/Sample2.py` - this will throw an exception
- `app/scripts/FakePythonJobs.py` - this will scrap [Fake Pyhon Jobs](https://realpython.github.io/fake-jobs/) site
