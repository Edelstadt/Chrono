#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import time

from funkce import slunecni_kruh, konkurenty, zlate_cislo, epakta_g, epakty_j
from funkce import velikonoce_j
from funkce import devitnik, misericordia, ctvrta_ned_ad


# vysledky overovany podle - Historicka chronologie, Marie Blahova, Libri, 2001
# pohyblive svatky (devitnik atd.) nejsou rozdeleny na jul. a greg. kal.,
# tudiz do roku 1583 maji spravne vysledky v jul. kal, pro roky vetsi v greg, kal
# Slo by to poupravit rozdelenim na 2 fce (stejne jak velikonoce), ale pro Ceske zeme to nema asi smysl
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
        self.assertEqual(time.strptime("1126-4-11", "%Y-%m-%d"), velikonoce_j(1126))
        self.assertEqual(time.strptime("1573-3-22", "%Y-%m-%d"), velikonoce_j(1573))
        self.assertEqual(time.strptime("1410-3-23", "%Y-%m-%d"), velikonoce_j(1410))
        self.assertEqual(time.strptime("1692-3-27", "%Y-%m-%d"), velikonoce_j(1692))
        self.assertEqual(time.strptime("1492-4-22", "%Y-%m-%d"), velikonoce_j(1492))

    def test_devitnik(self):
        self.assertEqual(time.strptime("1126-2-7", "%Y-%m-%d"), devitnik(1126))
        self.assertEqual(time.strptime("1666-2-21", "%Y-%m-%d"), devitnik(1666))
        self.assertEqual(time.strptime("1791-2-20", "%Y-%m-%d"), devitnik(1791))
        self.assertEqual(time.strptime("1272-2-21", "%Y-%m-%d"), devitnik(1272))
        self.assertEqual(time.strptime("1522-2-16", "%Y-%m-%d"), devitnik(1522))
        self.assertEqual(time.strptime("1764-2-19", "%Y-%m-%d"), devitnik(1764))
        self.assertEqual(time.strptime("1300-2-7", "%Y-%m-%d"), devitnik(1300))

    def test_misericordia(self):
        self.assertEqual(time.strptime("1126-4-25", "%Y-%m-%d"), misericordia(1126))
        self.assertEqual(time.strptime("1443-5-5", "%Y-%m-%d"), misericordia(1443))
        self.assertEqual(time.strptime("1737-5-5", "%Y-%m-%d"), misericordia(1737))
        self.assertEqual(time.strptime("1598-4-5", "%Y-%m-%d"), misericordia(1598))
        self.assertEqual(time.strptime("1690-4-9", "%Y-%m-%d"), misericordia(1690))

    def test_ctvrta_ned_ad(self):
        self.assertEqual(time.strptime("1737-12-22", "%Y-%m-%d"), ctvrta_ned_ad(1737))
        self.assertEqual(time.strptime("1957-12-22", "%Y-%m-%d"), ctvrta_ned_ad(1957))
        self.assertEqual(time.strptime("1348-12-21", "%Y-%m-%d"), ctvrta_ned_ad(1348))
        self.assertEqual(time.strptime("1511-12-21", "%Y-%m-%d"), ctvrta_ned_ad(1511))


if __name__ == '__main__':
    unittest.main()
