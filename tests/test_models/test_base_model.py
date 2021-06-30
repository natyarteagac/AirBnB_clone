#!/usr/bin/python3
"""
    Testing for BaseModel Class
"""
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel """

    def test_pep8(self):
        """ Testing pep8 in file"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_tring(TypeEr):
        if type(BaseModel.id) is not str():


if __name__ == '__main__':
    unittest.main()
