#!/usr/bin/python3
"""
    Testing for City Class
"""
import unittest
import pep8
from models.city import City


class Test_City(unittest.TestCase):
    """ Testing City """

    @classmethod
    def setUpClass(self):
        """
        setUpClass for create two instances for tests cases
        """
        self.my_model1 = City
        self.my_model2 = City

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
        result = pep8_style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if atributes are strings"""
        if type(self.my_model1) is str:
            self.assertTrue(self.my_model1.name)
            self.assertTrue(self.my_model1.state_id)

    def test_atributes(self):
        """Testing if atributes and datetime correspond to my_model1 and two"""
        self.assertTrue(hasattr(self.my_model1, "name"))
        self.assertTrue(hasattr(self.my_model1, "state_id"))


if __name__ == '__main__':
    unittest.main()
