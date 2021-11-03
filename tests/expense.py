import unittest
from expense import new_expense

class TestExpense(unittest.TestCase):

    def test_add_expense(self):
        self.assertEqual(new_expense(23, 'toto', 'PChojka'), True)
        self.assertEqual(new_expense('bonjour', 'toto', 'PChojka'), False) # Check that amount is an int
        self.assertEqual(new_expense(20, 23, 'PChojka'), False) # Check that label is a str
        self.assertEqual(new_expense(20, 'toto', 23), False) # Check that name is a str
        self.assertEqual(new_expense(20, 'toto', 'toto'), False) # Check that spender exist