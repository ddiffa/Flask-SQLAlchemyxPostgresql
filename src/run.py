import os

from app import create_app

if __name__ == '__main__':
    env_name = 'development'
    app = create_app(env_name)

    app.run()