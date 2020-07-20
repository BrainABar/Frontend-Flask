from app import create_app
'''
    This will run the flask app using the internal server
    It is not recommended to use it during production but useful during
    development.
    > export FLASK_APP=app.run.py
    > export FLASK_ENV=development
    > flask run
'''

if __name__ == '__main__':
    app = create_app()
    app.run()
