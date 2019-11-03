# JWT-Flask-SQLAlchemy

## Installation
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [Postgres](https://www.postgresql.org/) on your machine
  - Activate the project virtual environment with `$ pipenv shell` command
## Installing Project Dependencies
  - flask - Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
  - flask sqlalchemy - flask wrapper for Sqlalchemy, it adds Sqlalchemy support to flask apps
  - psycopg2 - python postgresql adapter that provides some commands for simple CRUD queries and more on postgresql db
  - flask-migrate - flask extension that handles SQLAlchemy database migration. Migration basically refers to the management of incremental, reversible changes to relational database schemas
  - flask-script - provides an extension for managing external scripts in flask. This is needed in running our db migrations from the command line
  - marshmallow - marshmallow is a library for converting complex datatypes to and from native Python datatypes. Simply put it is used for deserialization(converting data to application object) and serialization(converting application object to simple types).
  - pyjwt - python library to encode and decode JSON Web Tokens - We will use this token in verifying user's authenticity
  - Install all required dependencies with `$ pipenv install`
  - `$ pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow pyjwt`

## Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=postgres://name:password@houst:port/blog_api_db
      $ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
      ```
  - Start the app with `python run.py`
