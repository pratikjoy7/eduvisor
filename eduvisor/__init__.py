from eduvisor.config import Config
from eduvisor.web.controller import web
from eduvisor.admin.controller import admin
from eduvisor.db.models import db

from flask import Flask


app = Flask(__name__, template_folder='templates')
admin_app = Flask(__name__, template_folder='templates')
ctx = admin_app.app_context()
ctx.push()

app.config.from_object(Config)
admin_app.config.from_object(Config)

app.register_blueprint(web)
admin_app.register_blueprint(admin)

db.init_app(app)
db.init_app(admin_app)
