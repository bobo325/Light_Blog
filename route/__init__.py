from os import path
from flask import Blueprint

blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder=path.join('/templates/blog'),
    url_prefix='/blog')

from . import views