import unittest
from user import add_user

class TestUser(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('Max'), True)
        self.assertEqual(add_user(20), False) # Check that name is a str