import unittest
from datetime import date

from funkce import slunecni_kruh, konkurenty, zlate_cislo, epakta_g, epakty_j
from funkce import velikonoce_g, velikonoce_j
from funkce import devitnik, misericordia, ctvrta_ned_ad

class ChronoTest(unittest.TestCase):

    def test_slunecni_kruh(self):
        self.assertEqual(14, slunecni_kruh(341))
        self.assertEqual(15, slunecni_kruh(1126))
        self.assertEqual(24, slunecni_kruh(1583))
        self.assertEqual(8, slunecni_kruh(2015))

    def test_konkurenty(self):
        self.assertEqual(3, konkurenty(341))
        self.assertEqual(4, konkurenty(1126))
        self.assertEqual(1, konkurenty(1583))
        self.assertEqual(2, konkurenty(2015))

    def test_zlate_cislo(self):
        self.assertEqual(19, zlate_cislo(341))
        self.assertEqual(6, zlate_cislo(1126))
        self.assertEqual(7, zlate_cislo(1583))
        self.assertEqual(2, zlate_cislo(2015))

    def test_epakta(self):
        self.assertIsNone(epakta_g(341))
        self.assertIsNone(epakta_g(1126))
        self.assertEqual(7, epakta_g(1583))
        self.assertEqual(10, epakta_g(2015))

        self.assertEqual(18, epakty_j(19))
        self.assertEqual(25, epakty_j(6))
        self.assertEqual(6, epakty_j(7))
        self.assertEqual(11, epakty_j(2))

    def test_velikonoce(self):
        self.assertEqual('19.4.341', velikonoce_j(341))
        self.assertEqual('11.4.1126', velikonoce_j(1126))
        self.assertEqual('31.3.1583', velikonoce_j(1583))
        self.assertEqual('30.3.2015', velikonoce_j(2015))

        self.assertEqual('20.4.341', velikonoce_g(341))
        self.assertEqual('18.4.1126', velikonoce_g(1126))
        self.assertEqual('10.4.1583', velikonoce_g(1583))
        self.assertEqual('5.4.2015', velikonoce_g(2015))

    def test_devitnik(self):
        #TODO pro 341 exception! !!!
        #self.assertEqual(?, devitnik(341))
        self.assertEqual(date(1126, 2, 7), devitnik(1126))
        self.assertEqual(date(1583, 2, 6), devitnik(1583))
        self.assertEqual(date(2015, 2, 1), devitnik(2015))

    def test_misericordia(self):
        #TODO pro 341 exception! !!!
        #self.assertEqual(?, misericordia(341))
        self.assertEqual(date(1126, 4, 25), misericordia(1126))
        self.assertEqual(date(1583, 4, 24), misericordia(1583))
        self.assertEqual(date(2015, 4, 19), misericordia(2015))

    def test_ctvrta_ned_ad(self):
        #TODO funguje jen pro roky >1900 !!!!
        self.assertEqual(date(2015, 12, 20), ctvrta_ned_ad(2015))

if __name__ == '__main__':
    unittest.main()