""" Errors blueprint that will be the default served error page """
from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

bp = Blueprint('errors',
               __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/errors/static',)


@bp.before_request
def before_request(response):
    """ Before error request handler """
    print('test')


@bp.after_request
def after_request(response):
    """ After error request handler """
    print('test')


@bp.app_errorhandler(Exception)
def handle_exception(error):
    """ Default handler if none others match """

    # passes along HTTP errors
    if isinstance(error, HTTPException):
        return error

    # return render_template("500_generic.html", e=errror), 500
    # Handles non-HTTP exceptions
    return render_template('error_generic.html', title='500 error'), 500


@bp.app_errorhandler(400)
def bad_request(error):
    """ Default 400 error
        Manually call: abort(404, description='Manually called')
    """
    return '400 handled', 400


@bp.app_errorhandler(401)
def unauthorized(error):
    """ Default 404 error """
    return '401 handled', 401


@bp.app_errorhandler(403)
def forbidden(error):
    """ Default 403 error """
    return '403 handled', 403


@bp.app_errorhandler(404)
def not_found(error):
    """ Default 404 error
        Certain errors such as 404 are done at the global level
        and can't be specified within
    """
    return render_template('error_404.html'), 404


@bp.app_errorhandler(410)
def precondition_failed(error):
    """ Default 410 error """
    return '410 handled', 410


@bp.app_errorhandler(412)
def precondition_failed(error):
    """ Default 404 error """
    return '412 handled', 412


@bp.app_errorhandler(500)
def internal_server_error(error):
    """ Default 500 error
        In debug mode interactive debugger pops up instead
    """
    return '500 handled', 500


@bp.app_errorhandler(503)
def service_unavailable(error):
    """ Default 503 error """
    return '503 handled', 503