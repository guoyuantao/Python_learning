import unittest
from ex11_1.city_functions import city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):

        str_cc = city_country('santiago', 'chile')
        self.assertEqual(str_cc, 'Santiago,Chile')
if __name__ == '__main__':
    unittest.main()