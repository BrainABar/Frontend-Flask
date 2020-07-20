from flask import Flask
from app.blueprints import personal_bp, errors_bp


def create_app(environment: str = None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['CORS_HEADER'] = 'Content-Type'

    # overrides environment, if provided, otherwise tries to use FLASK_ENV
    if environment:
        app.config['ENV'] = environment

    # Load configuration based on export FLASK_ENV = ' '
    if app.config['ENV'] == 'production':
        app.config.from_object('app.config.ProductionConfig')
    elif app.config['ENV'] == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object('app.config.DevelopmentConfig')

    # Register blueprints
    app.register_blueprint(personal_bp, url_prefix='/')
    app.register_blueprint(errors_bp, url_prefix='/errors')

    return app
