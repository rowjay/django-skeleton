from django.conf.urls import url

from . import views

urlpatterns = [
    # This view is referenced from common_settings for the LOGIN_REDIRECT_URL
    # setting.
    # Make sure to update the references if you change or delete this url line!
    url(r"^$", views.home, name="home"),

    # Here are our example views. The name given is used by Django's reverse
    # url resolver to refer to the view. You can also reverse a url by
    # referring to the view function itself.
    url(r"objlist/$", views.list_objects, name="object_list"),
    url(r"objlist/new$", views.new_object, name="object_new"),

    # We use named regular expression capture groups because they're easier
    # to manage. We use the name "pk" here because that's the default keyword
    # that Django generic views look for
    url(r"objlist/(?P<pk>.+)/$", views.object_details, name="object_details"),
    url(r"objlist/(?P<pk>.+)/delete$", views.object_delete, name="object_delete"),
    url(r"objlist/(?P<pk>.+)/edit$", views.object_edit, name="object_edit"),
]
