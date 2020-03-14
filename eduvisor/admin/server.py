from eduvisor import admin_app
from eduvisor.config import Config

if __name__ == '__main__':
    admin_app.run(host='0.0.0.0', port=Config.ADMIN_PORT, debug=Config.DEBUG)
