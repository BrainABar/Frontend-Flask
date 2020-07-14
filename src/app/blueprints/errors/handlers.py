from flask import Blueprint, current_app, render_template

bp = Blueprint('errors',
               __name__,
               template_folder='templates',
               static_folder='static', )


@bp.app_errorhandler(404)
def handle404(error):
    return '404 handled', 404


@bp.app_errorhandler(500)
def internal_error(error):
    return '500 handled', 500

'''
@api.errorhandler(404)
def page_not_found(e):
    return 'error'
'''
