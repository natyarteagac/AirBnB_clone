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
        """ Testing pep8 style """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['base_model'])
        self.assertEqual(result.total_errors, 0)


if __name__ == '__main__':
    unittest.main()
