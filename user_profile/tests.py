from django.test import TestCase

from .models import *

# Create your tests here.
class StudentTestCase(TestCase):
    def test_save_method(self):
        student_Data=Student()
        with self.assertRaises(Exception):
            student_Data.save()


# Test Cases used for:
# 1. Field Validation
# 2.Data Retrieval
# 3.Form Validation
# 4.View Functionality
# 5.URL Routing
# 6.Authentication and Authorization
# 7.API Testing
# 8.Error Handling
# 9.File Uploads
# 10.Custom Logic and Business Rule
