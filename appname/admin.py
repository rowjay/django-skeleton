from django.contrib import admin

from . import models

"""
admin.py contains ModelAdmin classes that allow your database model classes
to be managed in Django's admin interface.

For basic functionality, you don't need to do anything but declare a blank
model admin and register it with a model. There are lots of  ways to
customize how your models interact with the admin interface.

See https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#modeladmin-objects
"""

@admin.register(models.MyObject)
class MyObjectAdmin(admin.ModelAdmin):
    pass
