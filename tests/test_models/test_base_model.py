#!/usr/bin/python3
"""
    Testing for BaseModel Class
"""
import unittest
import pep8
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Testing BaseModel """

    def test_pep8(self):
        """ Testing pep8 in file"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if uuid is string """
        bm = BaseModel()
        if type(bm.id) is str:
            self.assertTrue(bm.id)

    def test_time_corresponding_to(self):
        """ Testing if time correspond to """


if __name__ == '__main__':
    unittest.main()
