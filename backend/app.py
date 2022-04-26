from flask import Flask
from susej.extension import configuration
from susej.extension import database
# from susej.extension import manager_login
from susej.blueprint.api import product_resource
from susej.model import login 


app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
product_resource.init_app(app)
# manager_login.init_app(app)
login.init_app(app)
