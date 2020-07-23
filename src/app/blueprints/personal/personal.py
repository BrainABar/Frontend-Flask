""" Personal Pages Blueprint """

from typing import Any
from flask import Blueprint, render_template, abort


bp = Blueprint('personal', __name__,
               template_folder='templates',
               static_folder='static',
               static_url_path='/personal/static')


@bp.route('/', methods=['GET'])
def index() -> Any:
    """
    :return: Any
    """
    return render_template('index.html', title='Home')


@bp.route('/projects', methods=['GET'])
def projects() -> Any:
    """
    :return: Any
    """
    return render_template('projects.html', title='Projects')
