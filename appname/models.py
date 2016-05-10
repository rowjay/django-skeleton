from django.db import models
from django.core.urlresolvers import reverse

"""
This is your models.py file.

Django looks in this file for model definitions. A model definition is any
class that inherits from django.db.models.Model.

More information about defining models:
https://docs.djangoproject.com/en/1.9/intro/tutorial02/#creating-models

Remember if you change your models you need to create a migration and then
apply it, to update your database table schemas.

The command "manage.py makemigrations" looks at your migrations and your model
definitions and creates a new migration file for any changes that have been
made. This does not touch your database at all. You should check in to source
control any migration files in the same commit as the model changes.

The command "manage.py migrate" looks at your migrations and your database
and applies any migrations that have not been applied. Django keeps track of
which migrations have been applied in a special database table. You can undo
migrations by giving the migrate command an app name and a migration name to
rewind to.

More about migrations:
https://docs.djangoproject.com/en/1.9/topics/migrations/

"""


class MyObject(models.Model):
    """A simple example model used by the example views"""
    name = models.CharField(max_length=32)

    # A foreignkey to django's User model.
    owner = models.ForeignKey("auth.User")

    def get_absolute_url(self):
        """Return the url for a detail view for this object

        This is used by Django in a few places and, while it's not required,
        makes it convenient for constructing links to an object's details
        page, especially in templates, without having to remember which view
        to use.

        In other words, this method provides a single place to define which
        view to use as the detail view

        In particular, this method is used by default in Django's generic
        views to redirect to an object's details page after a create or update.
        """
        return reverse("object_details", args=[self.id])

    def __str__(self):
        """The default string representation of this object

        It's used in the admin interface, and when you do {{ object }} in a
        template, so you don't have to do {{ object.name }} everywhere.
        """
        return self.name