#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# final2.py
#
# Copyright 2013 Marcus Scalpere <marcus.scalpere@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import datetime
import time

"""Tento skript vypočítává chronologické pomůcky /
This script calculates the historical chronological utilities"""

#  slovníky k funkci nedelni_pismeno_g, podle staletí
VZOR_G_MAP = {
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
NEDELNI_PISMENO_G_2099_MAP = {
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

NEDELNI_PISMENO_G_1899_MAP = {
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

NEDELNI_PISMENO_G_1799_MAP = {
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

NEDELNI_PISMENO_G_1699_MAP = {
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

NEDELNI_PISMENO_J_MAP = [None, 'GF', 'E', 'D', 'C', 'BA', 'G', 'F', 'E', 'DC', 'B', 'A', 'G', 'FE', 'D', 'C', 'B',
                         'AG', 'F', 'E', 'D', 'CB', 'A', 'G', 'F', 'ED', 'C', 'B', 'A']


def slunecni_kruh(rok):
    """Tato funkce vypočítává sluneční kruh, parametr je rok/
    :param rok:
    This function calculates the solar circle, the parameter is the year"""
    return (rok + 9) % 28 or 28


def nedelni_pismeno_j(slunecnikruh):
    """Tato funkce vypočítává juliánské nedělní písmeno,
    :param slunecnikruh:
    parametr je sluneční kruh / Julian Dominical letter """
    return NEDELNI_PISMENO_J_MAP[slunecnikruh]


def konkurenty(rok):
    """Tato funkce vypočítává konkurenty,
    parametr je rok """
    ctvrtina = (rok / 4)
    ctvrtina = int(ctvrtina)
    return (rok + ctvrtina + 4) % 7 or 7


def zlate_cislo(rok):
    """Tato funkce vypočítává zlaté číslo,
    parametr je rok """
    cislo = (rok + 1) % 19
    if cislo == 0:
        return 19
    else:
        return cislo


def epakty_j(zlatecislo):
    """Tato funkce vypočítává juliánské epakty,
    parametr je zlaté číslo / jul. epacts"""
    return ((zlatecislo - 1) * 11) % 30


def epakta_g(rok):
    """Tato funkce vypočítává gregoriánské epakty,
    parametr je rok / greg. epacts """
    if rok <= 1582:
        return None
    else:
        stoleti = int(rok / 100) + 1
        opravas = int(3 * stoleti / 4)  # sluneční oprava
        opravam = int((8 * stoleti + 5) / 25)  # měsíční oprava
        return (epakty_j(zlate_cislo(rok)) - opravas + opravam + 8) % 30


def nedelni_pismeno_g(nedelni_p_j, rok):
    """Tato funkce počítá gregoriánské nedělní písmeno /
    greg. Dominical letter"""
    if rok <= 1582:
        return "Neni"
    else:
        if rok <= 1699:
            return NEDELNI_PISMENO_G_1699_MAP[nedelni_p_j]
        if rok <= 1799:
            return NEDELNI_PISMENO_G_1799_MAP[nedelni_p_j]
        if rok <= 1899:
            return NEDELNI_PISMENO_G_1899_MAP[nedelni_p_j]
        if rok <= 2099:
            return NEDELNI_PISMENO_G_2099_MAP[nedelni_p_j]


def velikonoce_j(rok):
    """Výpočet juliánské velikonoční neděle / jul. Easter"""
    pomocna_a = rok % 19
    pomocna_b = rok % 4
    pomocna_c = rok % 7
    pomocna_d = (15 + (19 * pomocna_a)) % 30
    pomocna_e = (6 + (2 * pomocna_b) + (4 * pomocna_c) + (6 * pomocna_d)) % 7
    if (22 + pomocna_d + pomocna_e) > 31:
        x = "%d-%d-%d" % (rok, 4, (pomocna_d + pomocna_e - 9))
        mezi = datetime.datetime.strptime(x, "%Y-%m-%d")
        t = mezi.timetuple()
        return t
    else:  # (22 + pomocna_d + pomocna_e) < 31:
        x = "%d-%d-%d" % (rok, 3, (22 + pomocna_d + pomocna_e))
        mezi = datetime.datetime.strptime(x, "%Y-%m-%d")
        t = mezi.timetuple()
        return t


def velikonoce_g(year):
    a = year % 19
    b = year >> 2
    c = b // 25 + 1
    d = (c * 3) >> 2
    e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
    e += (29578 - a - e * 32) >> 10
    e -= ((year % 7) + b - d + e + 2) % 7
    d = e >> 5
    day = e - d * 31
    month = d + 3
    x = "%d-%d-%d" % (year, month, day)
    mezi = datetime.datetime.strptime(x, "%Y-%m-%d")
    t = mezi.timetuple()
    return t


def velikonoce(rok):
    if rok < 1583:
        date_str = time.strftime("%Y-%m-%d", velikonoce_j(rok))
        dt = time.strptime(date_str, "%Y-%m-%d")
    else:
        date_str = time.strftime("%Y-%m-%d", velikonoce_g(rok))
        dt = time.strptime(date_str, "%Y-%m-%d")
    return datetime.date(dt[0], dt[1], dt[2])


def porovnani_odecteni(rok, mesic, den, den_pred):
    for x in range(1, 8):
        d1 = datetime.date(rok, mesic, den) - datetime.timedelta(days=x)
        d11 = d1.strftime('%w')
        d11 = int(d11)

        if d11 == den_pred:
            return d1


def porovnani_pricteni(rok, mesic, den, den_pred):
    for x in range(1, 8):
        d1 = datetime.date(rok, mesic, den) + datetime.timedelta(days=x)
        d11 = d1.strftime('%w')
        d11 = int(d11)

        if d11 == den_pred:
            return d1


def porovnani_odecteni_j(rok, mesic, den, den_pred):
    pismeno = nedelni_pismeno_j(slunecni_kruh(rok))
    rok2 = VZOR_G_MAP[pismeno]
    for x in range(1, 8):
        d1 = datetime.date(rok2, mesic, den) - datetime.timedelta(days=x)
        d11 = d1.strftime('%w')
        d11 = int(d11)
        d1 = d1.replace(year=rok)

        if d11 == den_pred:
            return d1


def porovnani_pricteni_j(rok, mesic, den, den_pred):
    pismeno = nedelni_pismeno_j(slunecni_kruh(rok))
    rok2 = VZOR_G_MAP[pismeno]
    for x in range(1, 8):
        d1 = datetime.date(rok2, mesic, den) + datetime.timedelta(days=x)
        d11 = d1.strftime('%w')
        d11 = int(d11)
        d1 = d1.replace(year=rok)

        if d11 == den_pred:
            return d1


def devitnik(rok):
    if rok == 1300 or rok == 1400 or rok == 1500:
        mezi = velikonoce(rok) - datetime.timedelta(days=62)
    else:
        mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 9))
    t = mezi.timetuple()
    return t


def nedele_po_devitniku(rok):
    if rok == 1300 or rok == 1400 or rok == 1500:
        mezi = velikonoce(rok) - datetime.timedelta(days=55)
    else:
        mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 8))
    t = mezi.timetuple()
    return t


def masopustni_nedele(rok):
    if rok == 1300 or rok == 1400 or rok == 1500:
        mezi = velikonoce(rok) - datetime.timedelta(days=48)
    else:
        mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 7))
    t = mezi.timetuple()
    return t


def popelecni_streda(rok):
    if rok == 1300 or rok == 1400 or rok == 1500:
        mezi = velikonoce(rok) - datetime.timedelta(days=45)
    else:
        mezi = velikonoce(rok) - datetime.timedelta(days=46)
    t = mezi.timetuple()
    return t


def prazna_nedele(rok):
    if rok == 1300 or rok == 1400 or rok == 1500:
        mezi = velikonoce(rok) - datetime.timedelta(days=41)
    else:
        mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 6))
    t = mezi.timetuple()
    return t


def druha_postni(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 5))
    t = mezi.timetuple()
    return t


def kychava_nedele(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 4))
    t = mezi.timetuple()
    return t


def druzebna_nedele(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 3))
    t = mezi.timetuple()
    return t


def smrtna_nedele(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 2))
    t = mezi.timetuple()
    return t


def kvetna_nedele(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=(7 * 1))
    t = mezi.timetuple()
    return t


def zeleny_ctvrtek(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=3)
    t = mezi.timetuple()
    return t


def velky_patek(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=2)
    t = mezi.timetuple()
    return t


def bila_sobota(rok):
    mezi = velikonoce(rok) - datetime.timedelta(days=1)
    t = mezi.timetuple()
    return t


def bila_nedele(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 1))
    t = mezi.timetuple()
    return t


def den_svatosti(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=12)
    t = mezi.timetuple()
    return t


def misericordia(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 2))
    t = mezi.timetuple()
    return t


def jubilate(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 3))
    t = mezi.timetuple()
    return t


def cantate(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 4))
    t = mezi.timetuple()
    return t


def krizova_nedele(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 5))
    t = mezi.timetuple()
    return t


def nanebevstoupeni(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=40)
    t = mezi.timetuple()
    return t


def exaudi(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 6))
    t = mezi.timetuple()
    return t


def letnice(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 7))
    t = mezi.timetuple()
    return t


def trojice(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=(7 * 8))
    t = mezi.timetuple()
    return t


def boziho_tela(rok):
    mezi = velikonoce(rok) + datetime.timedelta(days=60)
    t = mezi.timetuple()
    return t


def ctvrta_ned_ad(rok):
    for x in range(1, 8):
        if rok > 1582:
            d1 = datetime.date(rok, 12, 25) - datetime.timedelta(days=x)
            d11 = int(d1.strftime('%w'))
            if d11 == 0:
                t = d1.timetuple()
                return t
        else:
            pismeno = nedelni_pismeno_j(slunecni_kruh(rok))
            rok2 = VZOR_G_MAP[pismeno]
            d1 = datetime.date(rok2, 12, 25) - datetime.timedelta(days=x)
            d11 = int(d1.strftime('%w'))
            d1 = d1.replace(year=rok)
            if d11 == 0:
                t = d1.timetuple()
                return t


def treti_ned_ad(rok):
    date_str = time.strftime("%Y-%m-%d", ctvrta_ned_ad(rok))
    dt = time.strptime(date_str, "%Y-%m-%d")
    mezi = datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=7)
    t = mezi.timetuple()
    return t


def druha_ned_ad(rok):
    date_str = time.strftime("%Y-%m-%d", ctvrta_ned_ad(rok))
    dt = time.strptime(date_str, "%Y-%m-%d")
    mezi = datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=14)
    t = mezi.timetuple()
    return t


def prvni_ned_ad(rok):
    date_str = time.strftime("%Y-%m-%d", ctvrta_ned_ad(rok))
    dt = time.strptime(date_str, "%Y-%m-%d")
    mezi = datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=21)
    t = mezi.timetuple()
    return t


def nedele_letni(rok):
    nedele = []

    date_str = time.strftime("%Y-%m-%d", trojice(rok))
    dt = time.strptime(date_str, "%Y-%m-%d")
    date_str2 = time.strftime("%Y-%m-%d", prvni_ned_ad(rok))
    dt2 = time.strptime(str(date_str2), "%Y-%m-%d")
    dt2 = datetime.date(dt2[0], dt2[1], dt2[2]) + datetime.timedelta(days=0)
    for x in range(1, 40):
        d1 = datetime.date(dt[0], dt[1], dt[2]) + datetime.timedelta(days=7 * x)

        if d1 >= dt2:
            return nedele
        else:
            t = d1.timetuple()
            nedele.append(t)


def masopust(rok):
    # prázdný slovník
    nedele = []
    # zjištění první neděle po třech králích
    if rok < 1583:
        prvni = porovnani_pricteni_j(rok, 1, 6, 0)
    else:
        prvni = porovnani_pricteni(rok, 1, 6, 0)

    t = prvni.timetuple()
    # přidání první neděle do slovníku, index nedělí bude chronologicky
    nedele.append(t)
    # převod první neděle
    prvni = prvni.isoformat()
    dt_prvni = time.strptime(str(prvni), "%Y-%m-%d")
    date_str = time.strftime("%Y-%m-%d", devitnik(rok))
    # print(date_str)
    dt_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    # přidávání týdnů k první neděli
    for x in range(1, 15):
        d1 = datetime.datetime(dt_prvni[0], dt_prvni[1], dt_prvni[2]) + datetime.timedelta(
            days=7 * x)
        # pokud je výsledek shodný s poslední počítanou nedělí, tak ho zformátuj, přidej do slovníku a vrat slovník
        if d1 >= dt_obj:
            return nedele
        # pokud není, tak poslední počítanou neděli jen přidej do slovníku a pokračuj
        else:
            t = d1.timetuple()
            nedele.append(t)
