import json
import os


def load_config_from_json(filename, silent=False):
    try:
        with open(filename) as json_file:
            obj = json.loads(json_file.read())
            return obj
    except IOError as e:
        if silent:
            return False
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise


class Config(object):
    DEBUG = True
    TESTING = True

    SECRET_KEY = '\xdb{\xd9S\xd0\x9c\xe2\t\x913\xd0\x8d\xff\x06lBri\xf9\xe7\xd2?\x89\x86'

    GOOGLE_CLIENT_ID = '1075945838226-2qo66i98hk5k86ijipj8vscg094e7728.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '-j6INl8apVAXVzZ4lxqijAxA'
    OAUTH1_PROVIDER_ENFORCE_SSL = False

    PORT = 5000
    ADMIN_PORT = 5100

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://eduvisor_user:qweqwe@mysql/eduvisor'
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    locals().update(
        load_config_from_json('/opt/eduvisor/conf/eduvisor.json', silent=True) or {})
