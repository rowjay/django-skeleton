import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .common_settings import *

# Rename this file to settings.py to deploy this app.

# This file contains deployment-specific settings. It can also override any
# settings in common_settings.py
# You should leave this file out of source control (but still back it up
# somehow in production)

# You can run without adding anything to this file, but it's unsuitable for
# production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# The common settings file has defaults for development.
# Before deploying to production, uncomment and configure at least the
# following:

#DEBUG = False

# With DEBUG off, Django checks that the Host header in requests matches one of
# these. If you turn off DEBUG and you're suddenly getting HTTP 400 Bad
# Request responses, you need to add the host names to this list
#ALLOWED_HOSTS = []

# Set your production database parameters here! See
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
#DATABASE=...

# When DEBUG is off, these email addresses will receive an email for any
# unhandled exceptions while processing a request. See the logging
# configuration in common_settings for how that is set up.
ADMINS = [
    #('Admin Name', 'adminemail@example.com'),
]

