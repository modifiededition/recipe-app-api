################################################################################
####### Django built-in User Model ##################################################
################################################################################
################################################################################

# In Django, the User model is a built-in model provided by the django.contrib.auth module that represents a user account in your web application.
# It provides the necessary fields and functionality for user authentication, authorization, and user-related operations. Let's explore the User model in Django in detail:

#     Importing the User model:
#     To work with the User model, you need to import it from the django.contrib.auth module:

#     python

#     from django.contrib.auth.models import User

#     Fields in the User model:
#     The User model has several built-in fields to store user-related information. Some of the commonly used fields include:
#         username: A unique identifier for the user. It is typically used for user authentication and must be unique across all users.
#         password: Stores the hashed password for the user account. Django handles password hashing and provides methods to authenticate and validate passwords.
#         email: Stores the email address of the user.
#         first_name and last_name: Fields for storing the user's first name and last name.
#         is_active: A boolean field indicating whether the user account is active or not.
#         is_staff: A boolean field indicating whether the user has staff/admin privileges.
#         is_superuser: A boolean field indicating whether the user has superuser/admin privileges.

#     Authentication and Authorization:
#     The User model provides methods and attributes to handle user authentication and authorization, including:
#         User Registration: You can create new user accounts using the create_user() method or by directly instantiating the User model.
#         Authentication: The User model has a built-in authenticate() method to authenticate user credentials.
#         Authorization: You can check if a user has certain permissions or is part of specific user groups using methods like has_perm() and groups.

#     User Relationships:
#     The User model can be related to other models in your application. Common relationships include:
#         One-to-One: You can extend the User model by creating a separate model and linking it to the User model using a one-to-one relationship. This allows you to add
#         additional fields to the user profile.
#         Foreign Key: Other models in your application can have a foreign key relationship with the User model.
#         For example, a Post model might have a foreign key to the User model to indicate the author of the post.

#     Customizing the User Model:
#     Django allows you to customize the User model to fit your application's requirements.
#    You can create a custom user model by subclassing AbstractUser or AbstractBaseUser provided by the django.contrib.auth.models module.
#   This gives you more flexibility to add custom fields and methods to the User model.

#     User Authentication Views and Forms:
#     Django provides built-in views and forms for user authentication, such as login, logout, password reset, and registration.
#     You can use these views and forms to handle user authentication-related functionality in your web application.

#     Django Authentication Middleware:
#     Django includes authentication middleware that handles user authentication and maintains user sessions.
#     This middleware automatically associates a User instance with each request, making the user object available throughout the request-response cycle.

# The User model in Django is a crucial component for handling user-related operations in your web application, including user authentication, authorization, and user profile management.
# It simplifies the process of implementing user functionality and provides a secure and reliable way to manage user accounts.

################################################################################
###################### DJANGO USER MANAGER ################################################################################
################################################################################################################################################################
################################################################################

# In Django, the User Manager is a class that handles the creation, retrieval, and manipulation of user accounts in the Django authentication system.
# It is responsible for managing the user model instances and providing high-level methods for user-related operations. Let's explore the User Manager in Django in detail:

#     Default User Manager:
#     Django provides a default User Manager class called django.contrib.auth.models.UserManager. This manager class is automatically associated with the built-in User model and
#     provides methods for creating, retrieving, and managing user accounts.

#     Creating Custom User Managers:
#     Django allows you to create custom User Manager classes by subclassing django.contrib.auth.models.BaseUserManager and overriding specific methods.
#      This provides flexibility to customize the behavior of the User Manager according to your application's requirements.

#     User Manager Methods:
#     The User Manager provides several methods to perform operations on user accounts. Some commonly used methods include:
#         create_user(): Creates a new user account with the provided username and password. This method handles password hashing and user account creation.
#         create_superuser(): Creates a new superuser account with administrative privileges.
#         get_by_natural_key(): Retrieves a user instance based on the natural key, which is typically the username or email.
#         get_queryset(): Returns the queryset of user objects managed by the User Manager.
#         Additional methods: You can add custom methods to the User Manager to perform application-specific operations on user accounts.

#     Customizing User Managers:
#     By creating a custom User Manager class, you can add additional methods and behaviors to handle user-related operations specific to your application.
#     For example, you can add methods to search for users by specific criteria, filter users based on custom fields, or implement complex user creation logic.

#     Assigning Custom User Manager to User Model:
#     To use a custom User Manager with the User model, you need to specify it in the objects attribute of the User model. For example:

#     python

# class CustomUserManager(BaseUserManager):
#     # Custom manager methods and behaviors

# class CustomUser(AbstractBaseUser):
#     # User model fields and properties
#     objects = CustomUserManager()

# Registering Custom User Manager:
# If you have a custom User Manager class, you need to register it in the Django settings to be used as the default manager for the User model.
# Add the path to your custom User Manager class in the AUTH_USER_MODEL setting:

#     python

#     AUTH_USER_MODEL = 'myapp.CustomUser'

#     Replace 'myapp.CustomUser' with the actual path to your custom User model.

# The User Manager in Django plays a vital role in managing user accounts, providing methods for creating, retrieving, and manipulating user instances.
# It allows you to customize the behavior of user-related operations and implement application-specific functionality on top of the Django authentication system.