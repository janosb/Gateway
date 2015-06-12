DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'odetta',                      # Or path to database file if using sqlite3.
        'USER': 'odetta_user',                      # Not used with sqlite3.
        'PASSWORD': 'xxxx',                  # Not used with sqlite3.
        # 'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'HOST': 'scidb1.nersc.gov',
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}
