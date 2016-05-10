import django.forms

from . import models

"""
By convention, Django form classes are declared in this file.

Here we declare a single MyObjectForm, a ModelForm that provides a form from
the MyObject model.

A ModelForm will look a the referenced model class and automatically create
form fields from the corresponding fields on the model object. ModelForms
also know how to create and save the model objects with the form's .save()
method.

For forms that aren't a simple interface to a database model, you can create
a class that inherits from django.forms.Form and declare the fields yourself.

See https://docs.djangoproject.com/en/1.9/topics/forms/
"""

class MyObjectForm(django.forms.ModelForm):
    """A Model form for the MyObject model

    """
    class Meta:
        # This is where we declare what model this form is for, and what
        # fields to include in the form. Django generates a form by
        # translating the model fields to form fields.
        model = models.MyObject
        fields = ["name"]
