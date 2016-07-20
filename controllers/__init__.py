import jinja2
import os.path

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join([os.path.dirname(__file__), '..', 'views'])),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)