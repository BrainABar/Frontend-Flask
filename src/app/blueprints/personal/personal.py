from flask import Blueprint, render_template

bp = Blueprint('personal', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/personal/static')


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html', title='Contact')


@bp.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html', title='Projects')
