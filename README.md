# Frontend-Flask
Basic Flask application that will serve mostly static files.
Will be configured to serve its own files and be cached by nginx/varnished

Setup virtual enviroment:
```
> python3 -m virtualenv venv
> source venv/bin/activate
> python -m pip install -r requirements.txt
> python -m pip install --editable src/
```


Hosted on localhost:5000

To run Flask with live reloading:
```
> export FLASK_APP=src.app.run.py
> export FLASK_ENV=development
> flask run -h 0.0.0.0 -p 5000
```
To run Flask with Gunicorn in Docker (Uses Dockerfile in specified directory):
```
> docker build -t frontend-flask src/
> docker run -it -p 5000:5000 frontend-flask
```
Running flask with docker-containers :
```
> docker-compose up -d // include '--build' to force image rebuild
```