from eduvisor.web.authentication import requires_auth

from flask import Blueprint, current_app as app, render_template, session, url_for, redirect, request, flash
import requests
from requests_oauthlib import OAuth2Session

web = Blueprint('web', __name__, template_folder='templates')


@web.route('/login')
def login():
    if session.get('user'):
        return redirect(url_for('.auth', action='logout', _external=True))
    return render_template('login.html')


@web.route('/auth', defaults={'action': 'login'})
@web.route('/auth/<action>')
def auth(action):
    # Store some useful destinations in session
    if not request.args.get('state'):
        session['last'] = request.referrer or url_for('.index')
        if 'next' in request.args:
            session['next'] = url_for(request.args['next'])
        else:
            session['next'] = session['last']

    # User loggedin - logout &/or revoke
    if session.get('user'):
        if action == 'revoke':
            response = requests.get(
                'https://accounts.google.com/o/oauth2/revoke',
                params={'token': session['user']['token']['access_token']}
            )
            if response.status_code == 200:
                flash('Authorization revoked', 'warning')
            else:
                flash('Could not revoke token: {}'.format(response.content),
                      'danger')
        if action in ['logout', 'revoke']:
            del session['user']
            return redirect(url_for('.login', _external=True))
        return redirect(url_for('.index', _external=True))

    google = OAuth2Session(
        app.config['GOOGLE_CLIENT_ID'],
        scope=[
            'https://www.googleapis.com/auth/userinfo.email',
            'openid',
            'https://www.googleapis.com/auth/userinfo.profile',
        ],
        redirect_uri=url_for('.auth', _external=True),
        state=session.get('state')
    )

    # Initial client request, no `state` from OAuth redirect
    if not request.args.get('state'):
        url, state = google.authorization_url(
            'https://accounts.google.com/o/oauth2/auth',
            access_type='offline'
        )
        session['state'] = state
        return redirect(url)

    # Error returned from Google
    if request.args.get('error'):
        error = request.args['error']
        if error == 'access_denied':
            error = 'Not logged in'
        flash('Error: {}'.format(error), 'danger')
        return redirect(session['last'])

    # Redirect from google with OAuth2 state
    token = google.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        client_secret=app.config['GOOGLE_CLIENT_SECRET'],
        authorization_response=request.url
    )
    user = google.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
    user['token'] = token
    session['user'] = user

    return redirect(url_for('.index', _external=True))


@web.route('/', methods=['GET', 'POST'])
@requires_auth
def index():
    return render_template('web/index.html')
