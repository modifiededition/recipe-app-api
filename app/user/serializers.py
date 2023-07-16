"""
Serializers for the user API view.
"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )
from django.utils.translation import gettext as _
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password' : {'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password =  serializers.CharField(
        style = {"input_type":'passord'},
        trim_whitespace = False,
    )

    def validate(self, attrs):
        """Validate and autheticate the user."""
        email  = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request= self.context.get("request"),
            username = email,
            password = password,
        )
        if not user:
            msg = _("Unable to authenticate with provided credentials.")
            raise serializers.ValidationError(msg, code ='authorization')

        attrs['user'] = user
        return attrs




# In Django, a serializer is a crucial component of the Django REST Framework (DRF) that converts complex data types, such as querysets and
# model instances, into native Python data types that can be easily rendered into JSON, XML, or other content types.
# Serializers also handle parsing incoming data, such as JSON, and transforming it back into complex data types,
# which can then be used to create or update model instances.


# The primary use of serializers in Django is to facilitate the process of building Web APIs using Django REST Framework.
# Here are some of the key purposes and benefits of using serializers:

# Serialization: Serializers allow you to convert Django model instances, querysets,
# and other complex data structures into JSON or other content types.
# This is essential when you want to transmit data over the web, as most web clients understand and work with JSON data.

# Deserialization: Serializers handle the parsing of incoming data, such as JSON,
# and convert it into native Python data structures, making it easy to process
# and validate the data before saving it into the database.

# Integration with Views: Serializers are commonly used in combination with views to handle HTTP requests and
#  responses in a web API. They provide a consistent and clear way to transform data between Python objects and JSON.


# In Django REST Framework (DRF), ModelSerializer is a specialized serializer class that simplifies the process of working
# with Django models in the context of building Web APIs. It automatically generates serializer fields
# based on the model's fields, which can save a lot of boilerplate code when dealing with model instances.

# Let's walk through an example to see how ModelSerializer works:

# Suppose you have a simple Django model representing a book with the following fields:
# python
# models.py
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)
#     published_date = models.DateField()
#     is_published = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


# Now, you want to create a Web API to allow users to retrieve and create books. To do that,
# you need to create a serializer that translates the Book model into JSON and vice versa.

# Using ModelSerializer, you can achieve this with just a few lines of code:

# python

# # serializers.py
# from rest_framework import serializers
# from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = '__all__'


# In this example, we define a BookSerializer class that inherits from serializers.ModelSerializer.
# The Meta class inside the serializer specifies the model it's based on
# (Book) and the fields it should include in the serialized output (fields = '__all__').

# With this BookSerializer, you can now perform serialization and deserialization without writing additional code.
# For example, in your views, you can use this serializer to handle the data:

# python

# # views.py
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Book
# from .serializers import BookSerializer

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# In this example view, we use the BookSerializer to convert the queryset of books into JSON when handling the GET request.
# For the POST request, we use the serializer to deserialize the incoming JSON data, validate it, and save it as a new Book instance if valid.

# By using ModelSerializer, you get a lot of the serialization and validation logic for free.
# It's a powerful tool to quickly build Web APIs that work with Django models and maintain a clear and consistent codebase.
