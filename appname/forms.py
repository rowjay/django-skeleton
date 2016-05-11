import django.forms

from . import models

"""
By Django convention, form classes for an app are declared in a file called
forms.py

Here we declare a single MyObjectForm, a ModelForm that provides a form for
the MyObject model.

A ModelForm will inspect the referenced model class and automatically create
form fields from the corresponding fields on the model object. A ModelForm
also know how to create and save the model objects with the form's .save()
method.

For forms that aren't a simple interface to a database model, you can create
a class that inherits from django.forms.Form and declare the fields yourself.
You can then use the generic view FormView for use with regular forms.
CreateView and UpdateView are meant to work with model forms.

See https://docs.djangoproject.com/en/1.9/topics/forms/
and https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/
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
