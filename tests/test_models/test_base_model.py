#!/usr/bin/python3
"""
    Testing for BaseModel Class
"""
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Testing BaseModel """

    @classmethod
    def setUpClass(self):
        """
        setUpClass for create two instances for tests cases
        """
        self.my_model1 = BaseModel()
        self.my_model2 = BaseModel()

    @classmethod
    def tearDownClass(self):
        """
        tearDownClass for delete the instances for tests
        """
        del self.my_model1
        del self.my_model2

    """Testing BaseModel"""

    def test_pep8(self):
        """ Testing pep8 in file"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if uuid is string """
        if type(self.my_model1) is str:
            self.assertTrue(self.my_model1.id)

    def test_is_equal(self):
        """ Testing if time corresponds to """
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_atributes(self):
        """Testing if created_at correspond to my_model"""
        self.assertTrue(hasattr(self.my_model1, "created_at"))
        self.assertTrue(hasattr(self.my_model1, "updated_at"))
        self.assertTrue(hasattr(self.my_model1, "id"))
        self.assertIsInstance(self.my_model1.created_at, datetime)
        self.assertIsInstance(self.my_model1.updated_at, datetime)

    def test_checking_to_dict_representation(self):
        """Checking to dict representation"""
        if type(self.my_model1.to_dict) is dict:
            self.assertTrue(self.my_model1)


if __name__ == '__main__':
    unittest.main()
