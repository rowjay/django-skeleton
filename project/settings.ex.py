import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .common_settings import *

# Copy this file to settings.py to deploy this app.

# This file contains deployment-specific settings. It can also override any
# settings in common_settings.py
# You should leave settings.py out of source control (but still back
# it up somehow in production)

# You can run the django test server without adding anything to this file,
# but it's unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# Before deploying to production, uncomment and configure at least the
# following:

# Set this to False for production deployments
DEBUG = True

if DEBUG:
    LOGGING['root']['level'] = 'DEBUG'

# SECURITY WARNING: keep the secret key used in production secret!
# This generates a secret key the first time it's accessed. For production
# you will want to replace this entire block with something constant or
# pulled from the environment
# (because production deployments shouldn't have write access to the filesystem)
secret_key_path = os.path.join(BASE_DIR, "secret.txt")
if os.path.exists(secret_key_path):
    SECRET_KEY = open(secret_key_path, "r").read().strip()
else:
    import django.utils.crypto
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = django.utils.crypto.get_random_string(50, chars)
    # Create the file such that only the current user can read it
    fd = os.open(secret_key_path,
                 os.O_WRONLY|os.O_CREAT|os.O_TRUNC,
                 0o600)
    with os.fdopen(fd, "w") as keyout:
        keyout.write(SECRET_KEY)

# With DEBUG off, Django checks that the Host header in requests matches one of
# these. If you turn off DEBUG and you're suddenly getting HTTP 400 Bad
# Request responses, you need to add the host names to this list
#ALLOWED_HOSTS = []

# Set your production database parameters here! See
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
#DATABASES=...

def extra_context(request):
    """Extra context variables to include in every template context

    This function is referenced from the TEMPLATES setting from the common
    settings file
    """
    return {
        # Set this to your Google analytics key to enable google analytics in
        # your base template
        'GA': '',
    }

# When DEBUG is off, these email addresses will receive an email for any
# unhandled exceptions while processing a request. See the logging
# configuration in common_settings for how that is set up.
ADMINS = [
    #('Admin Name', 'adminemail@example.com'),
]

# Django's test server serves static files for you, but in production,
# Django expects your web server to take care of that. You will need to set
# STATIC_ROOT to a directory on your filesystem, and STATIC_URL to something
# like "/static/". Then configure your webserver to serve that directory at
# that url.
# Finally, run "manage.py collectstatic" and django will copy static files
# from various places into your STATIC_ROOT. You need to re-run collectstatic
# each time you redeploy with changes to static files.
#STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
#STATIC_URL = "/static/"

# Set your MEDIA_ROOT to some directory that's writable by your web server if
# your app involves writing to the filesystem using the default storage class
#MEDIA_ROOT = os.path.join(BASE_DIR, "files")

# Fill your google oauth2 credentials here if using oauth
# When creating the google oauth2 credentials, use this as the callback url:
# https://SERVER/oauth/provider/google/complete
#GOOGLE_OPENIDCONNECT_KEY = ""
#GOOGLE_OPENIDCONNECT_SECRET = ""

# To support sentry logging, uncomment these lines and set the DSN. You will
# need an account on a sentry server and create a project to get a DSN.
#
# You will also need to install the "raven" package in your virtualenv
# (remember to add it to your requirements.txt)
#
# Installing the raven_compat app will log all Django request handling
# exceptions (500 errors)
#
# You may also wish to install the raven logger to capture logging warnings
# or errors. Simply install a handler with class
# 'raven.contrib.django.raven_compat.handlers.SentryHandler' and configure a
# logger to use it.
#
# See https://docs.sentry.io/clients/python/integrations/django/
#
#INSTALLED_APPS.append("raven.contrib.django.raven_compat")
#import raven
#RAVEN_CONFIG = {
#    'dsn': '',
#    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
#}

# Uncomment for raven/sentry logging
# Install the "raven" package
#INSTALLED_APPS.append("raven.contrib.django.raven_compat")
#import raven
#RAVEN_CONFIG = {
#    'dsn': '', # FILL ME IN
#    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
#}

# If running under Amazon ELB or a proxy server not on localhost, uncomment
# this line for proper detection of SSL via the X-Forwarded-Proto header
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# To force SSL if the upstream proxy server doesn't do it for us, set this to
# True
#SECURE_SSL_REDIRECT = False

