import unittest
from ex11_3.employ import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employ = Employee('Jack', 'rose', 10000)

    def test_give_default_raise(self):
        self.assertEqual(self.employ.give_raise(), 15000)

    def test_give_custom_raise(self):
        self.assertEqual(self.employ.give_raise(10000), 20000)

if __name__ == '__main__':
    unittest.main()