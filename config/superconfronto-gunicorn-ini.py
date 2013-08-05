bind = "127.0.0.1:8000"

workers = 4

daemon = True

pidfile = '/opt/logs/superconfronto/gunicorn/gunicorn.pid'

loglevel = 'ERROR'

#accesslog = '/opt/logs/superconfronto/gunicorn/access.log'

errorlog = '/opt/logs/superconfronto/gunicorn/error.log'
