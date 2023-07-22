"""
Database models
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, email, password = None, **extra_field):
        """Create, save and return a new user."""

        user = self.model(email=self.normalize_email(email), **extra_field)
        if not email:
            raise ValueError("User must provide an email address.")
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user

## AbstractBaseUser: class contains functionalities for  authentication
## Permission Mixin: class contains functionalities for authorization

class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User in the system"""

    email = models.EmailField(max_length=255, unique=True) # passing unique = True as we want unique email into our database
    name  = models.CharField(max_length=255)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) ## default is False as we dont want any random user to give permissions of django-admin

    objects = UserManager()

    USERNAME_FIELD = 'email' ## this is to make sure instead of username we want email to for authorization purpose.

class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
