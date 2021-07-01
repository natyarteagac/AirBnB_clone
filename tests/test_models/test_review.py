#!/usr/bin/python3
"""
    Testing for User Class
"""
import unittest
import pep8
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Testing BaseModel """

    @classmethod
    def setUpClass(self):
        """
        setUpClass for create two instances for tests cases
        """
        self.my_model1 = Review()

    @classmethod
    def tearDownClass(self):
        """
        tearDownClass for delete the instances for tests
        """
        del self.my_model1

    """Testing BaseModel"""

    def test_pep8(self):
        """ Testing pep8 in file"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if atributes are strings"""
        if type(self.my_model1) is str:
            self.assertTrue(self.my_model1.place_id)
            self.assertTrue(self.my_model1.user_id)
            self.assertTrue(self.my_model1.text)


if __name__ == '__main__':
    unittest.main()
