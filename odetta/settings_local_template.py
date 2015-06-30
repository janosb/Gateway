DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'odetta',                      # Or path to database file if using sqlite3.
        'USER': 'odetta_user',                      # Not used with sqlite3.
        'PASSWORD': 'xxxx',                  # Not used with sqlite3.
        'HOST': 'scidb1.nersc.gov',
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# turn off extra url prefix
FORCE_SCRIPT_NAME = ''

# re-route to local static files
STATIC_URL = '/static/'

# where to upload files
STATIC_ROOT = ''

# where "home" will point
HOME_URL = '/'