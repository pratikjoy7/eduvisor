from sqlalchemy.orm.exc import NoResultFound

from eduvisor.db.models import AdminUsers

from functools import wraps
from flask import session, redirect, url_for


def is_admin():
    if not session.get('user'):
        return False
    try:
        AdminUsers.query.filter_by(email=session['user']['email']).one()
        return True
    except NoResultFound:
        return False


def requires_admin_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_admin():
            return redirect(url_for('.login', _external=True))
        return f(*args, **kwargs)
    return decorated
