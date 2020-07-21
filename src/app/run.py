"""
    Used by flask to run internal server
    It is not recommended to use it during production but useful during
    development.
    Errors might be given if setup.py is not used since src/ path is needed
    > export FLASK_APP=app.run.py
    > export FLASK_ENV=development
    > flask run
"""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()
