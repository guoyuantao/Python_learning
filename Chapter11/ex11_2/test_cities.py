import unittest
from ex11_2.city_function import city_country
class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):

        str_cc = city_country('santiago', 'chile')
        self.assertEqual(str_cc, 'Santiago, Chile')

    def test_city_country_population(self):
        str_c = city_country('santiago', 'chile', 'population=50000')
        self.assertEqual(str_c, 'Santiago, Chile Population=50000')
if __name__ == '__main__':
    unittest.main()