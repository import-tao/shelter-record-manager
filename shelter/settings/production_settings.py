from .base_settings import *
import dj_database_url
import django_heroku

def get_env_variable(var_name):
    '''Get environment variable or return exception. '''
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f'Set the {var_name} environment variable.'
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')
DATABASES = {'default': dj_database_url.config(default='postgres://user:pass@localhost/dbname')}

DEBUG = get_env_variable('DEBUG')

EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_PORT = get_env_variable('EMAIL_PORT')
EMAIL_USE_TLS = get_env_variable('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = get_env_variable('DEFAULT_FROM_EMAIL')

ALLOWED_HOSTS = ["*"]

django_heroku.settings(locals())
