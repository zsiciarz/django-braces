import os

from django.conf import settings


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))


if not settings.configured:
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django_nose',
        'braces',
    )
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS = INSTALLED_APPS,
        TEMPLATE_DIRS = (
            os.path.join(PROJECT_ROOT, 'braces', 'tests', 'templates'),
        ),
        SITE_ID = 1,
        ROOT_URLCONF = 'braces.tests.urls',
        TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
        NOSE_ARGS = ['--stop'],
    )


from django.core.management import call_command

call_command('test', 'braces')

