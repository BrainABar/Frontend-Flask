# Frontend-Flask
![CI](https://github.com/BrainABar/Frontend-Flask/workflows/CI/badge.svg?branch=master)

Basic Flask web application template that uses Docker and Jinja templates.

All options hosted on localhost:5000

Local Environment setup

Virtual environment:
```
> python3 -m pip install virtualenv
> python3 -m virtualenv venv
> source venv/bin/activate
> python -m pip install -r requirements.txt
> python -m pip install --editable src/
```

Run Flask with live reloading:
```
> export FLASK_APP=src.app.run.py
> export FLASK_ENV=development
> flask run -h 0.0.0.0 -p 5000
```

Run Gunicorn server:
```
> export FLASK_ENV=testing
> gunicorn -w 2 -b 0.0.0.0:5000 'app:create_app()'
```

Building Docker images:
```
> docker build -t frontend-flask src/
```

Another method is through Docker and Docker-Compose.
This allows for a similar environment from development to production.
The Dockerfile will setup the base environment and our Docker-Compose files can be linked to add additional
configurations as needed.

** include `--build` to force image rebuild

Run with flask server and live reloading:
```
> docker-compose -f docker-compose.yml -f docker-compose.fdev.yml up
```

Run with gunicorn server and live reloading:
```
> docker-compose -f docker-compose.yml -f docker-compose.gdev.yml up
```

Create enviroment to give commands such as pytest:
```
> docker-compose -f docker-compose.yml -f docker-compose.test.yml up
> pytest
```

Run with gunicorn server and Traefik configurations:
```
> docker network create reverse_proxy # If not created will throw an error since file relies on externally created network
> docker-compose -f docker-compose.yml -f docker-compose.production.yml up
```
