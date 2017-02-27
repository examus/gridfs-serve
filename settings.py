import sys

MONGO_DB_URL = 'mongodb://localhost:27017,localhost:27018/grid_fs?' \
               'replicaSet=test_set&readPreference=primaryPreferred'
# App section for builtin server
APP_HOST = '0.0.0.0'
APP_PORT = 5000
DEBUG = True

try:
    from settings_local import *
except ImportError:
    pass

if 'test' in sys.argv[0]:  # Is there another way?
    try:
        from settings_test import *
    except ImportError:
        pass
