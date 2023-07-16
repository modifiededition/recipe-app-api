"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

import time

from psycopg2 import OperationalError as Psycopg2Error

class Command(BaseCommand):
    """Django command to wait for database"""
    help = "This command is used to wait for the database until it gets configured!"

    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write("waiting for databse...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True

            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 sec.")
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))

# Django provides a feature called "custom management commands" that allows you to create your own commands to be executed 
# through the Django management interface. These custom commands can be used to perform various tasks such as database updates,
#  data processing, cron jobs, and more. Here's how you can create and use custom management commands in Django:

#     Create a Management Command:
#         In your Django project, create a directory called management inside your app directory (if it doesn't already exist).
#         Inside the management directory, create another directory called commands.
#         Inside the commands directory, create a Python module file with a descriptive name for your command, such as mycommand.py.

#     Define the Command:

#     Open the mycommand.py file and import the necessary Django modules:
#     python
# from django.core.management.base import BaseCommand

# Create a class that extends the BaseCommand class and override the handle() method. This method contains the logic for your command:

#     python
#     class Command(BaseCommand):
#         help = 'Description of your command'

#         def handle(self, *args, **options):
#             # Your command logic goes here
#             self.stdout.write("Command executed successfully")

#     Provide a brief description for your command in the help attribute of the command class.

# Register the Command:

#     To make your command discoverable, you need to include it in the INSTALLED_APPS setting of your Django project.
#     Open the settings.py file of your project and locate the INSTALLED_APPS list.
#     Add the dotted path to your app, followed by .management, to the INSTALLED_APPS list. For example:

#     python

#     INSTALLED_APPS = [
#         ...
#         'myapp.management',
#         ...
#     ]

# Run the Command:

#     Open a terminal or command prompt and navigate to your Django project directory.
#     Run the command using the following syntax:

#         python manage.py mycommand

#         Replace mycommand with the name you provided for your custom command.

# That's it! Your custom management command will be executed, and you'll see the output specified in the handle() method.
#  You can add any desired functionality to your custom command, such as interacting with models, making API calls, 
# or performing complex operations.