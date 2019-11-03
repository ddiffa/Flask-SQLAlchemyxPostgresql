# JWT-Flask-SQLAlchemy

## Installation
  - Install [Python](https://www.python.org/downloads/), [Pipenv](https://docs.pipenv.org/) and [Postgres](https://www.postgresql.org/) on your machine
  - Activate the project virtual environment with `$ pipenv shell` command
  - Install all required dependencies with `$ pipenv install`
  - `$ pipenv install flask flask-sqlalchemy psycopg2 flask-migrate flask-script marshmallow flask-bcrypt pyjwt`
  - Export the required environment variables
      ```
      $ export FLASK_ENV=development
      $ export DATABASE_URL=postgres://name:password@houst:port/blog_api_db
      $ export JWT_SECRET_KEY=hhgaghhgsdhdhdd
      ```
  - Start the app with `python run.py`
