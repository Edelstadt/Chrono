#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import operator

__title__ = 'chrono-tools'
__version__ = '0.0.2'
__author__ = 'Marek Dlabacek'
__license__ = 'BSD'
__copyright__ = 'Copyright 2013 Marek Dlabacek'

"""This script calculates the historical chronological
utilities"""

TRANS_TO_G_YEAR = 1583
#  slovníky k funkci nedelni_pismeno_g, podle staletí
PATTERN_G_MAP = {
    "A": 2006,
    "B": 2005,
    "C": 2010,
    "D": 2009,
    "E": 2003,
    "F": 2013,
    "G": 2001,
    "GF": 1996,
    "BA": 2000,
    "DC": 2004,
    "FE": 2008,
    "AG": 2012,
    "CB": 2016,
    "ED": 2020
}
DOMICAL_LETTER_G_2099_MAP = {
    "A": "G",
    "B": "A",
    "C": "B",
    "D": "C",
    "E": "D",
    "F": "E",
    "G": "F",
    "GF": "FE",
    "BA": "AG",
    "DC": "CB",
    "FE": "ED",
    "AG": "GF",
    "CB": "BA",
    "ED": "DC"
}

DOMICAL_LETTER_G_1899_MAP = {
    "A": "F",
    "B": "G",
    "C": "A",
    "D": "B",
    "E": "C",
    "F": "D",
    "G": "E",
    "GF": "ED",
    "BA": "GF",
    "DC": "BA",
    "FE": "DC",
    "AG": "FE",
    "CB": "AG",
    "ED": "CB",
}

DOMICAL_LETTER_G_1799_MAP = {
    "A": "E",
    "B": "F",
    "C": "G",
    "D": "A",
    "E": "B",
    "F": "C",
    "G": "D",
    "GF": "DC",
    "BA": "FE",
    "DC": "AG",
    "FE": "CB",
    "AG": "ED",
    "CB": "GF",
    "ED": "BA",
}

DOMICAL_LETTER_G_1699_MAP = {
    "A": "D",
    "B": "E",
    "C": "F",
    "D": "G",
    "E": "A",
    "F": "B",
    "G": "C",
    "GF": "CB",
    "BA": "ED",
    "DC": "GF",
    "FE": "BA",
    "AG": "DC",
    "CB": "FE",
    "ED": "AG",
}

DOMINICAL_LETTER_J_MAP = [None, 'GF', 'E', 'D', 'C', 'BA', 'G', 'F', 'E', 'DC',
                          'B', 'A', 'G', 'FE', 'D', 'C', 'B',
                          'AG', 'F', 'E', 'D', 'CB', 'A', 'G', 'F', 'ED', 'C',
                          'B', 'A']


class EasterTool():
    """
A tool for determining the date of Easter and the calculation of movable feasts
    """

    def __init__(self, year):
        self.__year = year

    def solar_circle(self):
        """
        This function calculates the solar circle, the parameter is the year"""
        return (self.__year + 9) % 28 or 28

    def dominical_letter_j(self):
        """
        :param solarcircle / Julian Dominical letter """
        return DOMINICAL_LETTER_J_MAP[self.solar_circle()]

    def concurrents(self):
        """Tato funkce vypočítává concurrents,
        parametr je year """
        quarter = (self.__year / 4)
        quarter = int(quarter)
        return (self.__year + quarter + 4) % 7 or 7

    def golden_number(self):
        """Tato funkce vypočítává zlaté číslo,
        parametr je year """
        number = (self.__year + 1) % 19
        if number == 0:
            return 19
        else:
            return number

    def epact_j(self):
        """Tato funkce vypočítává juliánské epakty,
        parametr je zlaté číslo / jul. epacts"""
        return ((self.golden_number() - 1) * 11) % 30

    def epact_g(self):
        """Tato funkce vypočítává gregoriánské epakty,
        parametr je year / greg. epacts """
        if self.__year <= TRANS_TO_G_YEAR:
            return None
        else:
            century = int(self.__year / 100) + 1
            correctionsolar = int(3 * century / 4)  # sluneční oprava
            correctionlunar = int((8 * century + 5) / 25)  # měsíční oprava
            return (self.epact_j() -
                    correctionsolar + correctionlunar + 8) % 30

    def dominical_letter_g(self):
        """Tato funkce počítá gregoriánské nedělní písmeno /
        greg. Dominical letter"""
        if self.__year <= TRANS_TO_G_YEAR:
            return "None"
        else:
            if self.__year <= 1699:
                return DOMICAL_LETTER_G_1699_MAP[self.dominical_letter_j()]
            if self.__year <= 1799:
                return DOMICAL_LETTER_G_1799_MAP[self.dominical_letter_j()]
            if self.__year <= 1899:
                return DOMICAL_LETTER_G_1899_MAP[self.dominical_letter_j()]
            if self.__year <= 2099:
                return DOMICAL_LETTER_G_2099_MAP[self.dominical_letter_j()]

    def easter_j(self):
        """Výpočet juliánské velikonoční neděle / jul. Easter"""
        help_a = self.__year % 19
        help_b = self.__year % 4
        help_c = self.__year % 7
        help_d = (15 + (19 * help_a)) % 30
        help_e = (6 + (2 * help_b) + (4 * help_c) + (6 * help_d)) % 7
        if (22 + help_d + help_e) > 31:
            date_fomat = "%d-%d-%d" % (self.__year, 4, (help_d + help_e - 9))
            to_tuple = datetime.datetime.strptime(date_fomat, "%Y-%m-%d")
            result_date = to_tuple.timetuple()
            return result_date
        else:  # (22 + help_d + help_e) < 31:
            date_fomat = "%d-%d-%d" % (self.__year, 3, (22 + help_d + help_e))
            to_tuple = datetime.datetime.strptime(date_fomat, "%Y-%m-%d")
            result_date = to_tuple.timetuple()
            return result_date

    def easter_g(self):
        """Výpočet gregoriánské velikonoční neděle / greg.. Easter"""
        help_a = self.__year % 19
        help_b = self.__year >> 2
        help_c = help_b // 25 + 1
        help_d = (help_c * 3) >> 2
        help_e = ((help_a * 19) - ((help_c * 8 + 5) // 25) + help_d + 15) % 30
        help_e += (29578 - help_a - help_e * 32) >> 10
        help_e -= ((self.__year % 7) + help_b - help_d + help_e + 2) % 7
        help_d = help_e >> 5
        day = help_e - help_d * 31
        month = help_d + 3
        result = "%d-%d-%d" % (self.__year, month, day)
        to_tuple = datetime.datetime.strptime(result, "%Y-%m-%d")
        date_format = to_tuple.timetuple()
        return date_format

    def easter(self):
        """Helper function for movable holidays
        Selects easter jul. or greg., depend on year change type cal."""
        if self.__year < TRANS_TO_G_YEAR:
            date_str = time.strftime("%Y-%m-%d", self.easter_j())
            date = time.strptime(date_str, "%Y-%m-%d")
        else:
            date_str = time.strftime("%Y-%m-%d", self.easter_g())
            date = time.strptime(date_str, "%Y-%m-%d")
        return datetime.date(date[0], date[1], date[2])

    def comparator(self, month, day, day_bef_aft, oper, *jg):
        """Helper function, Search the closest day of week by entering,
         oper 1 = -; 0 = +
        jg[0] = 0 = julian, jg[0] = 1 = greg."""
        year_org = self.__year
        if jg:
            if year_org < TRANS_TO_G_YEAR or jg[0] == 'J':
                letter = self.dominical_letter_j()
                year = PATTERN_G_MAP[letter]

        else:
            if year_org < TRANS_TO_G_YEAR:
                letter = self.dominical_letter_j()
                year = PATTERN_G_MAP[letter]

        if oper == 1:
            opr = operator.sub
        else:
            opr = operator.add

        for day_count in range(1, 8):
            date_1 = opr(datetime.date(year, month, day),
                         datetime.timedelta(days=day_count))
            date_2 = date_1.strftime('%w')
            date_2 = int(date_2)
            date_1 = date_1.replace(year=year_org)

            if date_2 == day_bef_aft:
                return date_1

    @staticmethod
    def moveable_feast(date, quantity_days, oper):
        """oper: 1 = +"""
        if oper == 1:
            result = date + datetime.timedelta(days=quantity_days)
        else:
            result = date - datetime.timedelta(days=quantity_days)
        return result.timetuple()

    def septuagesima(self):
        """Septuagesima/ devitnik"""
        if self.__year == 1300 or self.__year == 1400 or self.__year == 1500:
            return self.moveable_feast(self.easter(), 62, 0)

        else:
            return self.moveable_feast(self.easter(), (7 * 9), 0)

    def sexagesima(self):
        """Sexagesima/nedele po devitniku"""
        if self.__year == 1300 or self.__year == 1400 or self.__year == 1500:
            return self.moveable_feast(self.easter(), 55, 0)
        else:
            return self.moveable_feast(self.easter(), (7 * 8), 0)

    def quinquagesina(self):
        """Quinquagesina/masopustni nedele"""
        if self.__year == 1300 or self.__year == 1400 or self.__year == 1500:
            return self.moveable_feast(self.easter(), 48, 0)
        else:
            return self.moveable_feast(self.easter(), (7 * 7), 0)

    def dies_cinerum(self):
        """Ash Wednesday/popeleční středa"""
        if self.__year == 1300 or self.__year == 1400 or self.__year == 1500:
            return self.moveable_feast(self.easter(), 45, 0)
        else:
            return self.moveable_feast(self.easter(), 46, 0)

    def reminiscere(self):
        """Reminiscere/prazna nedele"""
        if self.__year == 1300 or self.__year == 1400 or self.__year == 1500:
            return self.moveable_feast(self.easter(), 41, 0)
        else:
            return self.moveable_feast(self.easter(), (7 * 6), 0)

    def second_sun_lent(self):
        """"Druhá postní neděle"""
        return self.moveable_feast(self.easter(), (7 * 5), 0)

    def kychava_nedele(self):
        return self.moveable_feast(self.easter(), (7 * 4), 0)

    def druzebna_nedele(self):
        return self.moveable_feast(self.easter(), (7 * 3), 0)

    def smrtna_nedele(self):
        return self.moveable_feast(self.easter(), (7 * 2), 0)

    def kvetna_nedele(self):
        return self.moveable_feast(self.easter(), (7 * 1), 0)

    def zeleny_ctvrtek(self):
        return self.moveable_feast(self.easter(), 3, 0)

    def velky_patek(self):
        return self.moveable_feast(self.easter(), 2, 0)

    def bila_sobota(self):
        return self.moveable_feast(self.easter(), 1, 0)

    def bila_nedele(self):
        return self.moveable_feast(self.easter(), (7 * 1), 1)

    def den_svatosti(self):
        return self.moveable_feast(self.easter(), 12, 1)

    def misericordia(self):
        """misericordia"""
        return self.moveable_feast(self.easter(), (7 * 2), 1)

    def jubilate(self):
        """jubilate"""
        return self.moveable_feast(self.easter(), (7 * 3), 1)

    def exaudi(self):
        """exaudi"""
        return self.moveable_feast(self.easter(), (7 * 6), 1)

    def letnice(self):
        """pentecostes"""
        return self.moveable_feast(self.easter(), (7 * 7), 1)

    def trojice(self):
        """Trinity Sunday"""
        return self.moveable_feast(self.easter(), (7 * 8), 1)

    def boziho_tela(self):
        """Solemnity of the Body and Blood of Christ"""
        return self.moveable_feast(self.easter(), 60, 1)

    def ctvrta_ned_ad(self):
        """4. advent Sunday"""
        for day_count in range(1, 8):
            if self.__year > TRANS_TO_G_YEAR:
                date_1 = datetime.date(self.__year, 12, 25) \
                         - datetime.timedelta(days=day_count)
                date_2 = int(date_1.strftime('%w'))
                if date_2 == 0:
                    result = date_1.timetuple()
                    return result
            else:
                pismeno = self.dominical_letter_j()
                year2 = PATTERN_G_MAP[pismeno]
                date_1 = datetime.date(year2, 12, 25) \
                    - datetime.timedelta(days=day_count)
                date_2 = int(date_1.strftime('%w'))
                date_1 = date_1.replace(year=self.__year)
                if date_2 == 0:
                    result = date_1.timetuple()
                    return result

    def treti_ned_ad(self):
        """3. advent Sunday"""
        date_str = time.strftime("%Y-%m-%d", self.ctvrta_ned_ad())
        date = time.strptime(date_str, "%Y-%m-%d")
        to_tuple = datetime.date(date[0], date[1], date[2]) \
                   - datetime.timedelta(days=7)
        result = to_tuple.timetuple()
        return result

    def druha_ned_ad(self):
        """2. advent Sunday"""
        date_str = time.strftime("%Y-%m-%d", self.ctvrta_ned_ad())
        date = time.strptime(date_str, "%Y-%m-%d")
        to_tuple = datetime.date(date[0], date[1], date[2]) \
                   - datetime.timedelta(days=14)
        result = to_tuple.timetuple()
        return result

    def prvni_ned_ad(self):
        """1. advenresult Sunday"""
        date_str = time.strftime("%Y-%m-%d", self.ctvrta_ned_ad())
        date = time.strptime(date_str, "%Y-%m-%d")
        to_tuple = datetime.date(date[0], date[1], date[2]) \
                   - datetime.timedelta(days=21)
        result = to_tuple.timetuple()
        return result

    def nedele_letni(self):
        nedele = []
        date_str = time.strftime("%Y-%m-%d", self.trojice())
        date = time.strptime(date_str, "%Y-%m-%d")
        date_str2 = time.strftime("%Y-%m-%d", self.prvni_ned_ad())
        date2 = time.strptime(str(date_str2), "%Y-%m-%d")
        date2 = datetime.date(date2[0], date2[1], date2[2]) \
                + datetime.timedelta(days=0)
        for day_count in range(1, 40):
            date_1 = datetime.date(date[0], date[1], date[2]) \
                     + datetime.timedelta(days=7 * day_count)

            if date_1 >= date2:
                return nedele
            else:
                result = date_1.timetuple()
                nedele.append(result)

    def masopust(self):
        # prázdný slovník
        sunday = []
        # zjištění první neděle po třech králích

        first_sunday = self.comparator(1, 6, 0, 0)

        result = first_sunday.timetuple()
        # přidání první neděle do slovníku, index nedělí bude chronologicky
        sunday.append(result)
        # převod první neděle
        first_sunday = first_sunday.isoformat()
        date_first_sunday = time.strptime(str(first_sunday), "%Y-%m-%d")
        date_str = time.strftime("%Y-%m-%d", self.septuagesima())
        # print(date_str)
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        # přidávání týdnů k první neděli
        for day_count in range(1, 15):
            date1 = datetime.datetime(date_first_sunday[0],
                                      date_first_sunday[1],
                                      date_first_sunday[2])
            date_1 = self.moveable_feast(date1, (7 * day_count), 1)
            # pokud je výsledek shodný s poslední počítanou nedělí,
            # tak ho zformátuj, přidej do slovníku a vrat slovník

            date_1 = datetime.datetime.fromtimestamp(time.mktime(date_1))
            if date_1 >= date_obj:
                return sunday
            # pokud není, tak poslední počítanou neděli
            # jen přidej do slovníku a pokračuj
            else:
                result = date_1.timetuple()
                sunday.append(result)