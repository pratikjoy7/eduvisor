from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import Board, Zilla, Upazilla, Institution, Result, AdminUsers
