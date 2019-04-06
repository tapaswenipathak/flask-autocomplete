Flask Autocomplete
-------------------

This project is a web app that renders a autocomplete widget: as the user
types, it shows a list of results, just like what you'd expect from the Google
Search autocomplete.

# Setup and Installation

Install `pipenv`:

```sh
pip install --user pipenv
```

Then, install the project's dependencies:

```sh
pipenv install
```

And activate the project's virtualenv:

```sh
pipenv shell
```

# Running the server

```sh
python app.py
```

Then load <http://localhost:8000/>

# Code Layout

## Server
* `app.py` API route for autocomplete

## Client
* `static/index.html` HTML loaded at root URL
* `static/script.js` Javascript file loaded by index.html
* `static/styles.css` CSS file loaded by index.html
