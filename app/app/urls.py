"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name = 'api-schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name= "api-schema"), name = 'api-docs'
    ),
    path('api/user/', include('user.urls')),
    path('api/recipe/', include('recipe.urls')),

]



# In Django, views are Python functions or classes that receive web requests and return web responses.
# They are responsible for handling the logic of processing requests, interacting with models and databases
# ,and generating appropriate responses to be sent back to the client.

# Django views can be created using functions or classes, with classes being the more powerful and flexible option.
# Let's dive into the details of Django views:

# Function-based Views:
# Function-based views are defined as Python functions that take a request object as a parameter and
#  return a response object. The request object represents the incoming HTTP request from the client, and the response object contains the data to be sent back to the client.

# Here's an example of a simple function-based view that returns a basic HTTP response:

# python

# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello, World!")


# Class-based Views:
# Class-based views (CBVs) are more powerful and provide a structured way to handle different HTTP methods (GET, POST, etc.) \
# and encapsulate related functionality.
# CBVs are defined as classes that inherit from Django's View class or one of its subclasses.

# CBVs can define methods that correspond to different HTTP methods and handle the processing logic accordingly.
# For example, the get() method handles GET requests, the post() method handles POST requests, and so on.
# CBVs provide a clean separation of concerns and allow for code reuse through inheritance.

# Here's an example of a class-based view that handles GET and POST requests:

# python

# from django.views import View
# from django.http import HttpResponse

# class GreetingView(View):
#     def get(self, request):
#         return HttpResponse("Hello, GET!")

#     def post(self, request):
#         return HttpResponse("Hello, POST!")


# Request and Response Objects:
# Django provides request and response objects to handle HTTP requests and responses.

#     Request Object: The request object encapsulates the data of an incoming HTTP request. It contains information such as the request method (GET, POST, etc.),
#     headers, user authentication details, GET and POST parameters, and more. Views access this object to extract relevant data from the request.

#     Response Object: The response object represents the data to be sent back to the client as an HTTP response. It can be a simple text response,
#     an HTML page, a JSON object, or a redirect to another URL. Views create and return this response object, which Django then sends back to the client.

# URL Mapping:
# Views are associated with specific URLs through URL patterns defined in Django's URL configuration. URL patterns map specific URLs to their corresponding views, allowing Django to determine which view should handle a particular request.

# URL patterns can be defined using regular expressions or simpler path patterns. Here's an example of how a URL pattern is mapped to a view:

# python

# from django.urls import path
# from .views import hello

# urlpatterns = [
#     path('hello/', hello),
# ]

# In this example, the URL pattern /hello/ is mapped to the hello function-based view.



# Context and Templates:
# Views can pass data to HTML templates to generate dynamic web pages. Views typically fetch data from models or perform other processing and
# then pass the data to the template for rendering. Django provides a templating engine that allows you to combine HTML templates with Python code to generate dynamic content.

# Views use the render() function or the TemplateResponse class to render templates and return the rendered content as an HTTP response.

# Here's an example of a view that renders a template and passes context data:

# python

#     from django.shortcuts import render

#     def hello(request):
#         context = {'name': 'John'}
#         return render(request, 'hello.html', context)

#     In this example, the hello.html template is rendered with the name variable available in the template for dynamic content.

# Django views are the core components responsible for handling requests, processing data, and generating responses.
# They provide a flexible way to define the logic of your application and interact with other Django components like models, forms, and templates.
