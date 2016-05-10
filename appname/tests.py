from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from . import models

"""
Test cases for the app are placed in this file. You can run all tests with
manage.py test
"""

class TestExampleApp(TestCase):
    """This is an example test case, that works against the sample views

    It shows how to use the django test client to simulate actual requests"""

    def setUp(self):
        """This is run before every test"""
        # Here we create a new user and log them in to the test client.
        # Because the database is wiped clean after every test, we have to
        # create a new user here.
        self.user = User(username="User 1")
        self.user.save()

        self.client.force_login(self.user)

    def test_new(self):
        """Tests the object_new view"""
        # Here we will make sure the new view works. First we want to assert
        # that the database is empty. The default test runner gives us a
        # clean database before every test, but let's just be sure.
        self.assertEqual(
            0,
            models.MyObject.objects.count(),
        )

        # Now let's hit the view and make sure the response is a 200 OK
        response = self.client.post(
            reverse("object_new"),
            {
                "name": "My Object Name",
            },
            # Set follow to True because it may actually return a 302 redirect
            follow=True,
        )
        self.assertEqual(
            200,
            response.status_code
        )

        # The response was good, but did it actually create an object?
        self.assertEqual(
            1,
            models.MyObject.objects.count(),
        )

        # Let's take a closer look at that object
        obj = models.MyObject.objects.get()
        self.assertEqual(
            self.user,
            obj.owner,
        )
        self.assertEqual(
            "My Object Name",
            obj.name,
        )

        # And that's the gist of using the Django test runner and test
        # client. If this were an actual app, we'd want tests for the other
        # views, tests to make sure the right list of objects are returned in
        # the list view, that you can't edit someone else's object in the
        # delete or update views, etc.