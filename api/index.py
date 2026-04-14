import os
import sys
from django.core.wsgi import get_wsgi_application
from django.conf import settings

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bezbreda.settings')

# Configure settings for Vercel
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY=os.environ.get('SECRET_KEY', 'fallback-secret-key'),
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'agency',
        ],
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        ROOT_URLCONF='bezbreda.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ],
        WSGI_APPLICATION='bezbreda.wsgi.application',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # Use in-memory database for serverless
            }
        },
        STATIC_URL='static/',
        STATICFILES_DIRS=[os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static')],
        STATIC_ROOT=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles'),
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
    )

application = get_wsgi_application()

# Vercel expects a function called `handler`
def handler(request, **kwargs):
    from django.core.handlers.wsgi import WSGIHandler
    from django.http import HttpResponse

    # Create a WSGI environ from the Vercel request
    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query_string.decode('utf-8') if request.query_string else '',
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': str(len(request.body)) if request.body else '0',
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': request.body,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Add headers
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value

    # Handle the request
    handler = WSGIHandler()
    response = handler(environ, lambda status, headers: HttpResponse())

    return {
        'statusCode': int(response.status_code),
        'headers': dict(response.headers),
        'body': response.content.decode('utf-8'),
    }