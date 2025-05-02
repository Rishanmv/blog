import os
# ...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Add this
    'api',  # Add this
    'corsheaders', #add this
]
# ...
# Database configuration (PostgreSQL example)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',  # Replace with your database name
        'USER': 'your_username',      # Replace with your username
        'PASSWORD': 'your_password',  # Replace with your password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Add this for REST framework authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # Add this
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}

# Add this for Cross-Origin Resource Sharing
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Or the origin of your React app
    "http://127.0.0.1:3000",
]

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')