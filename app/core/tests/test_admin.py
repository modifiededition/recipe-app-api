"""
Tests for the Django admin modifications.
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client

class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse("admin:core_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)







###############################################################################################################
################### DJANGO ADMIN ##############################################
###############################################################################################################

# Django Admin is a powerful feature of the Django web framework that provides a ready-to-use administrative interface for managing and interacting with your Django application's data.
# It allows you to perform CRUD (Create, Read, Update, Delete) operations on your models without having to build a separate user interface from scratch. Here are the key aspects and
# features of Django Admin:

#     Enabling Django Admin:
#     To enable the Django Admin interface, you need to perform the following steps:
#         Add 'django.contrib.admin' to the INSTALLED_APPS list in your project's settings.py file.
#         Ensure that the 'django.contrib.admin' middleware is included in the MIDDLEWARE list in your settings.py file.
#         Run the command python manage.py migrate to apply the necessary database migrations.

#     Registering Models:
#     To make your models accessible in the Django Admin interface, you need to register them in the appropriate admin.py file within your app. In this file,
#       you can define a custom ModelAdmin class to specify the desired behavior and appearance for your model.
#         Create an admin.py file in your app directory (if it doesn't already exist).
#         Import your models and the admin module:

#         python

# from django.contrib import admin
# from .models import YourModel

# Register your models by subclassing admin.ModelAdmin and defining the desired behavior:

# python

#         @admin.register(YourModel)
#         class YourModelAdmin(admin.ModelAdmin):
#             # Customize the admin interface for your model
#             list_display = ['field1', 'field2', ...]
#             list_filter = ['field1', 'field2', ...]
#             search_fields = ['field1', 'field2', ...]
#             # More options...

#     Accessing the Django Admin Interface:
#
#     You can access the Django Admin interface by running your Django development server and navigating to the /admin URL in your browser.
#
#     For example: http://localhost:8000/admin

#     Features of Django Admin Interface:
#     The Django Admin interface provides various features to manage your data efficiently:
#         Model Listing: The Admin interface displays a list view of your registered models, showing the records and their corresponding fields.
#         CRUD Operations: You can create, read, update, and delete records directly through the interface.
#         Search and Filtering: Django Admin allows you to search for specific records based on fields and apply filters to narrow down the results.
#         Sorting and Pagination: You can sort the records based on specific fields and paginate through the results.
#         Model Relationships: Django Admin handles model relationships such as foreign keys, many-to-many relationships, and inline editing.
#         Customization: You can customize the appearance and behavior of your models in the Admin interface by overriding methods and specifying options in the ModelAdmin class.
#         Permissions and User Management: Django Admin integrates with Django's authentication system, allowing you to assign permissions and manage users
#         who can access the administrative interface.

#     Customizing the Admin Interface:
#     Django Admin provides several ways to customize the interface according to your application's requirements:
#         Overriding Methods: You can override various methods in the ModelAdmin class to change the behavior of specific actions, such as saving models or displaying data.
#         ModelAdmin Options: You can specify various options in the ModelAdmin class, such as list_display, list_filter, search_fields, readonly_fields, fieldsets, etc.,
#         to customize the display and behavior of your models in the Admin interface.
#         Custom Templates: You can create custom templates for specific models or override the default admin templates to change the look and feel of the interface.

# Django Admin provides a convenient and feature-rich administrative interface out-of-the-box, allowing you to manage your application's data efficiently.
# It saves time and effort by handling common CRUD operations and providing customization options for a tailored user experience.




###############################################################################################################
################### DJANGO TEST CLIENT ##############################################
###############################################################################################################


# django test client force login method
# ChatGPT

# In Django, the test client provided by the django.test.Client class allows you to simulate and test HTTP requests and responses in your Django application.
# # To simulate a logged-in user during testing, you can use the force_login() method provided by the test client. This method allows you to
# # authenticate a user without requiring actual authentication credentials. Here's how you can use the force_login() method:

#     Import the Required Modules:
#     To use the test client and the force_login() method, you need to import the necessary modules:

#     python

# from django.test import Client
# from django.contrib.auth.models import User

# Create and Authenticate a User:
# Before using the force_login() method, you need to create a user instance and authenticate it. You can use the Django User model or any custom user model you have defined.

# python

# def test_my_view():
#     user = User.objects.create_user(username='testuser', password='testpass')
#     client = Client()
#     client.force_login(user)
#     # Test code

# In this example, a new user is created using the create_user() method of the User model. You can provide the desired username and password for the test user.

# Use the force_login() Method:
# Once the user is created and authenticated, you can use the force_login() method of the test client to simulate a logged-in user for your test.

# python

# def test_my_view():
#     user = User.objects.create_user(username='testuser', password='testpass')
#     client = Client()
#     client.force_login(user)

#     response = client.get('/my_view/')  # Example URL
#     # Assert statements and further test code

# In this example, the force_login() method is called with the authenticated user object. This sets the user as the authenticated user for the test client.

# Performing Tests:
# After using the force_login() method, you can perform your tests by making requests through the test client, simulating the behavior of an authenticated user.

# python

#     def test_my_view():
#         user = User.objects.create_user(username='testuser', password='testpass')
#         client = Client()
#         client.force_login(user)

#         response = client.get('/my_view/')  # Example URL

#         assert response.status_code == 200
#         # More assertions and test code

#     In this example, a GET request is made to /my_view/, and the response is stored in the response variable. You can then use assertions and further test code to verify the behavior of your view.

# The force_login() method is a useful tool in testing Django views that require authentication. It allows you to simulate the behavior of authenticated users without needing actual user credentials.