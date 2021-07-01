#!/usr/bin/python3
"""
    Testing for State Class
"""
import unittest
import pep8
from models.state import State


class Test_State(unittest.TestCase):
    """ Testing State """

    @classmethod
    def setUpClass(self):
        """
        setUpClass for create two instances for tests cases
        """
        self.my_model1 = State
        self.my_model2 = State

    @classmethod
    def tearDownClass(self):
        """
        tearDownClass for delete the instances for tests
        """
        del self.my_model1
        del self.my_model2

    def test_pep8(self):
        """ Testing pep8 in file"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if atributes are strings"""
        if type(self.my_model1) is str:
            self.assertTrue(self.my_model1.name)

    def test_atributes(self):
        """Testing if atributes and datetime correspond to my_model1 and two"""
        self.assertTrue(hasattr(self.my_model1, "name"))


if __name__ == '__main__':
    unittest.main()
