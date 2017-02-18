#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest

from Chrono_Tool import EasterTool

# verification results by - Historicka chronologie, Marie Blahova, Libri, 2001

test_year_341 = EasterTool(341)
test_year_1126 = EasterTool(1126)
test_year_1583 = EasterTool(1583)
test_year_2015 = EasterTool(2015)
test_year_1573 = EasterTool(1573)
test_year_1410 = EasterTool(1410)
test_year_1692 = EasterTool(1692)
test_year_1666 = EasterTool(1666)
test_year_1791 = EasterTool(1791)
test_year_1272 = EasterTool(1272)
test_year_1522 = EasterTool(1522)
test_year_1764 = EasterTool(1764)
test_year_1300 = EasterTool(1300)
test_year_1443 = EasterTool(1443)
test_year_1737 = EasterTool(1737)
test_year_1598 = EasterTool(1598)
test_year_1690 = EasterTool(1690)
test_year_1957 = EasterTool(1957)
test_year_1348 = EasterTool(1348)
test_year_1511 = EasterTool(1511)
test_year_1492 = EasterTool(1492)


class ChronoTest(unittest.TestCase):
    def test_solar_circle(self):
        self.assertEqual(14, test_year_341.solar_circle())
        self.assertEqual(15, test_year_1126.solar_circle())
        self.assertEqual(24, test_year_1583.solar_circle())
        self.assertEqual(8, test_year_2015.solar_circle())

    def test_concurrents(self):
        self.assertEqual(3, test_year_341.concurrents())
        self.assertEqual(4, test_year_1126.concurrents())
        self.assertEqual(1, test_year_1583.concurrents())
        self.assertEqual(2, test_year_2015.concurrents())

    def test_golden_number(self):
        self.assertEqual(19, test_year_341.golden_number())
        self.assertEqual(6, test_year_1126.golden_number())
        self.assertEqual(7, test_year_1583.golden_number())
        self.assertEqual(2, test_year_2015.golden_number())

    def test_epact_g(self):
        self.assertIsNone(test_year_341.epact_g())
        self.assertIsNone(test_year_1126.epact_g())
        self.assertIsNone(test_year_1583.epact_g())
        self.assertEqual(10, test_year_2015.epact_g())

    def tests_epact_j(self):
        self.assertEqual(18, test_year_341.epact_j())
        self.assertEqual(25, test_year_1126.epact_j())
        self.assertEqual(6, test_year_1583.epact_j())
        self.assertEqual(11, test_year_2015.epact_j())

    def test_easter_j(self):
        self.assertEqual(time.strptime("1126-4-11", "%Y-%m-%d"),
                         test_year_1126.easter_j())
        self.assertEqual(time.strptime("1573-3-22", "%Y-%m-%d"),
                         test_year_1573.easter_j())
        self.assertEqual(time.strptime("1410-3-23", "%Y-%m-%d"),
                         test_year_1410.easter_j())
        self.assertEqual(time.strptime("1692-3-27", "%Y-%m-%d"),
                         test_year_1692.easter_j())
        self.assertEqual(time.strptime("1492-4-22", "%Y-%m-%d"),
                         test_year_1492.easter_j())

    def test_septuagesima(self):
        self.assertEqual(time.strptime("1126-2-7", "%Y-%m-%d"),
                         test_year_1126.septuagesima())
        self.assertEqual(time.strptime("1666-2-21", "%Y-%m-%d"),
                         test_year_1666.septuagesima())
        self.assertEqual(time.strptime("1791-2-20", "%Y-%m-%d"),
                         test_year_1791.septuagesima())
        self.assertEqual(time.strptime("1272-2-21", "%Y-%m-%d"),
                         test_year_1272.septuagesima())
        self.assertEqual(time.strptime("1522-2-16", "%Y-%m-%d"),
                         test_year_1522.septuagesima())
        self.assertEqual(time.strptime("1764-2-19", "%Y-%m-%d"),
                         test_year_1764.septuagesima())
        self.assertEqual(time.strptime("1300-2-7", "%Y-%m-%d"),
                         test_year_1300.septuagesima())

    def test_misericordia(self):
        self.assertEqual(time.strptime("1126-4-25", "%Y-%m-%d"),
                         test_year_1126.misericordia())
        self.assertEqual(time.strptime("1443-5-5", "%Y-%m-%d"),
                         test_year_1443.misericordia())
        self.assertEqual(time.strptime("1737-5-5", "%Y-%m-%d"),
                         test_year_1737.misericordia())
        self.assertEqual(time.strptime("1598-4-5", "%Y-%m-%d"),
                         test_year_1598.misericordia())
        self.assertEqual(time.strptime("1690-4-9", "%Y-%m-%d"),
                         test_year_1690.misericordia())

    def test_ctvrta_ned_ad(self):
        self.assertEqual(time.strptime("1737-12-22", "%Y-%m-%d"),
                         test_year_1737.ctvrta_ned_ad())
        self.assertEqual(time.strptime("1957-12-22", "%Y-%m-%d"),
                         test_year_1957.ctvrta_ned_ad())
        self.assertEqual(time.strptime("1348-12-21", "%Y-%m-%d"),
                         test_year_1348.ctvrta_ned_ad())
        self.assertEqual(time.strptime("1511-12-21", "%Y-%m-%d"),
                         test_year_1511.ctvrta_ned_ad())


if __name__ == '__main__':
    unittest.main()
