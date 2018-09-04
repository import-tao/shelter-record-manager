from .base_settings import *
import dj_database_url


def get_env_variable(var_name):
    '''Get environment variable or return exception. '''
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f'Set the {var_name} environment variable.'
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')
DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}

DEBUG = False

ALLOWED_HOSTS = []