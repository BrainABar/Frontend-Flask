from flask import Flask

def create_app():
    from app.blueprints.personal import personal_bp
    from app.blueprints.errors import errors_bp
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(personal_bp, url_prefix='/')
    app.register_blueprint(errors_bp, url_prefix='/errors')
    app.config['CORS_HEADER'] = 'Content-Type'
    return app
