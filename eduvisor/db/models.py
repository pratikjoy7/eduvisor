from eduvisor.db import db


class Board(db.Model):
    __tablename__ = 'board'
    board_id = db.Column('board_id', db.Integer, primary_key=True)
    board_name = db.Column('board_name', db.String(50), unique=True)


class Zilla(db.Model):
    __tablename__ = 'zilla'
    zilla_id = db.Column('zilla_id', db.Integer, primary_key=True)
    zilla_name = db.Column('zilla_name', db.String(50), unique=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))


class Upazilla(db.Model):
    __tablename__ = 'upazilla'
    upazilla_id = db.Column('upazilla_id', db.Integer, primary_key=True)
    upazilla_name = db.Column('upazilla_name', db.String(50), unique=True)
    zilla_id = db.Column(db.Integer, db.ForeignKey('zilla.zilla_id'))


class Institution(db.Model):
    __tablename__ = 'institution'
    eiin = db.Column('eiin', db.Integer, primary_key=True)
    institution_name = db.Column('institution_name', db.String(50), unique=True)
    upazilla_id = db.Column(db.Integer, db.ForeignKey('upazilla.upazilla_id'))


class Result(db.Model):
    __tablename__ = 'result'
    result_id = db.Column('result_id', db.Integer, primary_key=True)
    exam_year = db.Column('exam_yar', db.DateTime)
    exam_type = db.Column('exam_type', db.String(3))
    total_gpa5 = db.Column('total_gpa5', db.Integer)
    total_appeared = db.Column('total_appeared', db.Integer)
    total_passed = db.Column('total_passed', db.Integer)
    pass_percentage = db.Column('pass_percentage', db.Float)
    eiin = db.Column(db.Integer, db.ForeignKey('institution.eiin'))


class AdminUsers(db.Model):
    __tablename__ = 'admin_users'

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(50))
