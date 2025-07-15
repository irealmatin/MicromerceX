import environ

# init environ
env = environ.Env()

# read .env file
environ.Env.read_env('.env') 

PIPELINE = env('PIPELINE', default='local')

if PIPELINE == 'production':
    from .production import *
else:
    from .local import *


