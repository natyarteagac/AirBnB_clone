#!/usr/bin/python3
"""
    Testing for Place Class
"""
import unittest
import pep8
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Testing Place """

    @classmethod
    def setUpClass(self):
        """
        setUpClass for create two instances for tests cases
        """
        self.my_model1 = Place
        self.my_model2 = Place

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
        result = pep8_style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_uuid_is_string(self):
        """ Testing if atributes are strings"""
        if type(self.my_model1) is str:
            self.assertTrue(self.my_model1.city_id)
            self.assertTrue(self.my_model1.user_id)
            self.assertTrue(self.my_model1.name)
            self.assertTrue(self.my_model1.amenity)

    def test_uuid_is_integers(self):
        """ Testing if atributes are integers"""
        if type(self.my_model1) is int:
            self.assertTrue(self.my_model1.numers_rooms)
            self.assertTrue(self.my_model1.number_bathrooms)
            self.assertTrue(self.my_model1.max_guest)
            self.assertTrue(self.my_model1.price_by_night)

    def test_uuid_is_float(self):
        """ Testing if atributes are float"""
        if type(self.my_model1) is float:
            self.assertTrue(self.my_model1.latitude)
            self.assertTrue(self.my_model1.longitude)

    def test_atributes(self):
        """Testing if atributes and datetime correspond to my_model1 and two"""
        self.assertTrue(hasattr(self.my_model1, "city_id"))
        self.assertTrue(hasattr(self.my_model1, "user_id"))
        self.assertTrue(hasattr(self.my_model1, "name"))
        self.assertTrue(hasattr(self.my_model1, "description"))
        self.assertTrue(hasattr(self.my_model1, "number_rooms"))
        self.assertTrue(hasattr(self.my_model1, "number_bathrooms"))
        self.assertTrue(hasattr(self.my_model1, "max_guest"))
        self.assertTrue(hasattr(self.my_model1, "price_by_night"))
        self.assertTrue(hasattr(self.my_model1, "latitude"))
        self.assertTrue(hasattr(self.my_model1, "longitude"))
        self.assertTrue(hasattr(self.my_model1, "amenity_ids"))


if __name__ == '__main__':
    unittest.main()
