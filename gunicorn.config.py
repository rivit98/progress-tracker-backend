bind = "0.0.0.0:8000"
workers = 2
# certfile = '/home/rivit/certificate/cpt-rest.pem'
# keyfile = '/home/rivit/certificate/cpt-rest.key'
errorlog = './gunicorn/error.log'
accesslog = './gunicorn/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# daemon = True
