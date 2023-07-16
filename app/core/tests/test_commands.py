"""
Test custom Django managment commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command("wait_for_db")
        
        patched_check.assert_called_once_with(databases=['default'])
    
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting Operational Error"""

        patched_check.side_effect = [Psycopg2Error]*2 + \
                [OperationalError] *3 +[True]
        
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.asset_called_with(databases=['default'])



# In Django, mocking and patching are commonly used techniques in unit testing to isolate specific parts of code and
# simulate their behavior. The mock.patch function from the unittest.mock module allows you to replace objects or 
# functions with mock objects, enabling you to control their behavior during testing.
# Let's explore the mock.patch function in more detail:


# Importing the Required Modules:
# To use the mock.patch function, you need to import the unittest.mock module:

# python

# from unittest import mock

# Patching Objects or Functions:
# The mock.patch function is used as a decorator or a context manager to replace objects or functions with mock objects. 
# It takes the target object or function as an argument and returns a mock object. There are different ways to apply the patch:

# a) Patching as a Decorator:

    # python

    # @mock.patch('module.path.to.object')
    # def test_function(mock_object):
    #     # Test code

# This applies the patch to the specified object during the execution of the decorated test function. The patch is automatically applied and reverted for each test.

    # b) Patching as a Context Manager:

    # python

    # def test_function():
    #     with mock.patch('module.path.to.object') as mock_object:
    #         # Test code

# Here, the patch is applied within the context manager block. It allows more fine-grained control over when the patch is active and reverted.

# Configuring Mock Behavior:
# The mock object returned by mock.patch allows you to configure its behavior. You can set return values, define side effects, and check how the object was called. Some commonly used methods and attributes include:

#     return_value: Sets the return value of the mock object.

# python

# mock_object.return_value = 42

#     side_effect: Assigns a function or an iterable to be called or iterated over when the mock object is called.

# python

# mock_object.side_effect = lambda x: x * 2

#     assert_called(), assert_called_with(): Checks if the mock object was called, and if so, with the specified arguments.

# python

# mock_object.assert_called()
# mock_object.assert_called_with(10, 'test')

# Patching Class Methods:
# When patching class methods, you need to specify the class name and the method name in the patch path.

# python

# @mock.patch('module.path.to.Class.method')
# def test_function(mock_method):
#     # Test code

# Patching Multiple Objects:
# You can patch multiple objects or functions by using multiple decorators or context managers, or by passing a list of patch paths.

# python

# @mock.patch('module.path.to.object1')
# @mock.patch('module.path.to.object2')
# def test_function(mock_object1, mock_object2):
#     # Test code

# Cleaning Up:
# When using the mock.patch decorator or context manager, the patch is automatically reverted after the test or the block execution. However, if you need to manually revert a patch, you can use the stop() method on the mock object.

# python

#     def test_function():
#         patch_object = mock.patch('module.path.to.object')
#         mock_object = patch_object.start()
#         # Test code
#         patch_object.stop()

# The mock.patch function is a powerful tool for isolating code during testing by replacing objects or functions with controlled mock objects. It allows you to simulate specific scenarios and behavior, making it easier to write
    




