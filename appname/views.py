import django.views.generic
import django.contrib.auth.mixins
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from . import models
from . import forms

"""
views.py - holds the view code for your Django app

Views are functions responsible for taking a request object and returning a
response object. The routing of URLs to views is defined in your urls.py file.

We like to use Django Class-based Views. They are a little confusing but
basically, a hierarchy of Python classes each provide bits of functionality
that together make the view function. With class based views, the view
function is returned from the class's as_view() classmethod.

When a class-based view is invoked, a dispatch() method is called,
which looks at the HTTP request method and dispatches to e.g. a get() or a
post() method.

The views in the django.views.generic module provide base functionality for
rendering templates, retrieving objects from a database, processing forms,
etc. With Django's generic views, you typically only need to define one or
two class attributes, and override one or two methods to have a working view.

For more information about class based views, see
https://docs.djangoproject.com/en/1.9/topics/class-based-views/

A good reference for the generic class based views Django provides is
https://ccbv.co.uk/

This views.py file comes with some examples to illustrate how they work. You
are free to use simple functions where they make sense, but we illustrate some
common patterns with class based views here.
"""

class Home(django.views.generic.TemplateView):
    """This is an example Template view. It provides functionality to render
    a template in a context. The only required item is a "template_name"
    attribute.

    You can add more items to the template context by overriding the
    get_context_data() method.
    """
    template_name = "home.html"
# This is the view function that is actually referenced by the urls.py url
# configuration
home = Home.as_view()


class ObjectListView(django.contrib.auth.mixins.LoginRequiredMixin,
                     django.views.generic.ListView):
    """This is an example list view. It provides functionality to get a list
    of objects from the database and render a template in a context that
    includes that object list.

    The only required attributes are "template_name" and a "model" attribute
    that tells it which model we're listing.

    The class definition shows how multiple inheritance can be used to add
    functionality. The LoginRequiredMixin class requires the user to be
    logged in. If they aren't, it redirects them to the url specified in the
    LOGIN_URL setting, which we have set to the "login" view.

    """
    model = models.MyObject
    template_name = "examples/my_object_list.html"

    def get_queryset(self):
        """Override to only list items that are owned by the current user

        This method is called by ListView to get the queryset to use in the
        template context. We add a filter to only get objects owned by
        the current user according to the "owner" field on our MyObject model.

        """
        qs = super().get_queryset()
        # we can assume request.user exists because we mixed in the
        # LoginRequiredMixin to this class, so only logged in users can get
        # this far.
        return qs.filter(owner=self.request.user)
list_objects = ObjectListView.as_view()

class ObjectCreateView(django.contrib.auth.mixins.LoginRequiredMixin,
                       django.views.generic.CreateView):
    """This view controls the creation of a new MyObject object

    This view provides a GET handler that shows an html form, and a POST
    handler that creates a new object on valid form or shows the form with
    errors on invalid forms.

    Here we explicitly specify the form class to use--the CreateView will
    generate one for you if you don't specify one. See forms.py for information
    on MyObjectForm
    """
    model = models.MyObject
    form_class = forms.MyObjectForm
    template_name = "examples/my_object_new.html"

    def form_valid(self, form):
        """This is called by CreateView on a POST request after the form has
        been validated.

        This method's job is to save the object to the database and then
        return an HttpResponse object, usually a redirect.

        Here we override the default functionality to set the "owner" field
        before we save it to the database.

        """
        # The form class, since it's a ModelForm, can create and save the
        # object for us. However, we tell it to create but not save the
        # object by using commit=False so we can edit it before saving it.
        self.object = form.save(commit=False)

        # Now set the owner field and save
        self.object.owner = self.request.user
        self.object.save()

        # This saves any many-to-many fields on the model. The example model
        # doesn't have any, but you should call this any time you use
        # form.save() with commit=False, after you save the object manually.
        # See https://docs.djangoproject.com/en/1.9/topics/forms/modelforms/#the-save-method
        form.save_m2m()

        # get_success_url() will look at the self.success_url class attribute,
        # and if that doesn't exist, tries to call
        # self.object.get_absolute_url(), which we have defined on the model.
        return HttpResponseRedirect(self.get_success_url())
new_object = ObjectCreateView.as_view()

class ObjectDetailView(django.contrib.auth.mixins.LoginRequiredMixin,
                       django.views.generic.DetailView):
    """This view shows details about an object.

    The generic DetailView gets an object from the database and inserts it
    into the template context as the variable "object".

    We override the get_queryset() just the same as the list view to only
    allow viewing details of objects owned by the current owner.

    """
    model = models.MyObject
    template_name = "examples/my_object_detail.html"

    def get_queryset(self):
        # Same queryset we used for the list view
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        """An example on how to add additional items to a template context"""
        kwargs["my_context_var"] = "Hello, world!"
        return super().get_context_data(**kwargs)
object_details = ObjectDetailView.as_view()

class ObjectDeleteView(django.contrib.auth.mixins.LoginRequiredMixin,
                       django.views.generic.DeleteView):
    """This view deletes an object when it receives an HTTP POST or DELETE

    When responding to a GET request, it shows a confirmation form using the
    given template

    """
    model = models.MyObject
    template_name = "examples/my_object_delete_confirm.html"
    # We have to define where to redirect to after deletion is successful. We
    # can either define a success_url or override get_success_url().
    # Here we must use reverse_lazy() instead of reverse() because the url
    # subsystem may not be loaded at the time this class is defined,
    # which is when the module is imported.
    success_url = reverse_lazy("object_list")

    def get_queryset(self):
        # Same queryset we used for the list view
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
object_delete = ObjectDeleteView.as_view()

class ObjectEditView(django.contrib.auth.mixins.LoginRequiredMixin,
                     django.views.generic.UpdateView):
    """This shows an edit form for an object, and updates the object on POST"""
    model = models.MyObject
    template_name = "examples/my_object_edit.html"
    # We can re-use the same form class from the new form. UpdateView
    # knows how to pass in the existing data and instance to the form class.
    form_class = forms.MyObjectForm
    def get_queryset(self):
        # By now we ought to be sick of copy pasting this method on all our
        # views that operate on existing objects or object lists. A better
        # solution would be to make our own mixin class that defines this
        # method, and have all of our views (besides CreateView) inherit from
        # it!
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
object_edit = ObjectEditView.as_view()