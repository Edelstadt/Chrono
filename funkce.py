#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  final2.py
#
#  Copyright 2013 Marcus Scalpere <marcus.scalpere@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
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


NEDELNI_PISMENO_J_MAP = [None,'GF', 'E', 'D', 'C', 'BA', 'G', 'F', 'E', 'DC', 'B', 'A', 'G', 'FE', 'D', 'C', 'B',
 'AG', 'F', 'E', 'D', 'CB', 'A', 'G', 'F', 'ED', 'C', 'B', 'A']


def slunecni_kruh(rok):
    """Tato funkce vypočítává sluneční kruh, parametr je rok/
    This function calculates the solar circle, the parameter is the year"""
    return (rok + 9) % 28 or 28


def nedelni_pismeno_j(slunecnikruh):
    """Tato funkce vypočítává juliánské nedělní písmeno,
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
        return "%d.%d.%d" % ((pomocna_d + pomocna_e - 9), 4, rok)
    else:# (22 + pomocna_d + pomocna_e) < 31:
        return "%d.%d.%d" % ((22 + pomocna_d + pomocna_e), 3, rok)


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
    return "%d.%d.%d" % (day, month, year)


def velikonoce(rok):
    if rok < 1583:
        dt = time.strptime(str(velikonoce_j(rok)), "%d.%m.%Y")
    else:
        dt = time.strptime(str(velikonoce_g(rok)), "%d.%m.%Y")
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
    return velikonoce(rok) - datetime.timedelta(days=(7*9))

def nedele_po_devitniku(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*8))

def masopustni_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*7))

def popelecni_streda(rok):
    return velikonoce(rok) - datetime.timedelta(days=(46))

def prazna_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*6))

def druha_postni(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*5))

def kychava_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*4))

def druzebna_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*3))

def smrtna_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*2))

def kvetna_nedele(rok):
    return velikonoce(rok) - datetime.timedelta(days=(7*1))

def zeleny_ctvrtek(rok):
    return velikonoce(rok) - datetime.timedelta(days=(3))

def velky_patek(rok):
    return velikonoce(rok) - datetime.timedelta(days=(2))

def bila_sobota(rok):
    return velikonoce(rok) - datetime.timedelta(days=(1))

def bila_nedele(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*1))

def den_svatosti(rok):
    return velikonoce(rok) + datetime.timedelta(days=(12))

def misericordia(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*2))

def jubilate(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*3))

def cantate(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*4))

def krizova_nedele(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*5))

def nanebevstoupeni(rok):
    return velikonoce(rok) + datetime.timedelta(days=(40))

def exaudi(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*6))

def letnice(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*7))

def trojice(rok):
    return velikonoce(rok) + datetime.timedelta(days=(7*8))

def boziho_tela(rok):
    return velikonoce(rok) + datetime.timedelta(days=(60))

def ctvrta_ned_ad(rok):
    for x in range(1, 8):
        if rok > 1582:
            d1 = datetime.date(rok, 12, 25) - datetime.timedelta(days=x)
            d11 = int(d1.strftime('%w'))
            if d11 == 0:
                return d1
        else:
            pismeno = nedelni_pismeno_j(slunecni_kruh(rok))
            rok2 = VZOR_G_MAP[pismeno]
            d1 = datetime.date(rok2, 12, 25) - datetime.timedelta(days=x)
            d11 = int(d1.strftime('%w'))
            d1 = d1.replace(year=rok)
            if d11 == 0:
                    return d1

def treti_ned_ad(rok):
    dt = time.strptime(str(ctvrta_ned_ad(rok)), "%Y-%m-%d")
    return datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=7)

def druha_ned_ad(rok):
    dt = time.strptime(str(ctvrta_ned_ad(rok)), "%Y-%m-%d")
    return datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=14)

def prvni_ned_ad(rok):
    dt = time.strptime(str(ctvrta_ned_ad(rok)), "%Y-%m-%d")
    return datetime.date(dt[0], dt[1], dt[2]) - datetime.timedelta(days=21)

def nedele_letni(rok):
    nedele = []
    dt = time.strptime(str(trojice(rok)), "%Y-%m-%d")
    for x in range(1, 40):
        d1 = datetime.date(dt[0], dt[1], dt[2]) + datetime.timedelta(days=7*x)
        if d1 == prvni_ned_ad(rok):
            return nedele
        else:
            d11 = d1.isoformat()
            nedele.append(d11)

def masopust(rok):
    nedele = [] #prázdný slovník
    if rok < 1583:
        prvni = porovnani_pricteni_j(rok, 1, 6, 0) #zjištění první neděle po třech králích
    else:
        prvni = porovnani_pricteni(rok, 1, 6, 0) #zjištění první neděle po třech králích
    pokus = time.strptime(str(devitnik(rok)), "%Y-%m-%d") #výpočet popeleční středy a rodělení do slovníku
    #posledni = porovnani_odecteni(pokus[0], pokus[1], pokus[2], 0) #zjištění první neděle před popeleční středou
    prvni = prvni.isoformat() #převod první neděle
    nedele.append(prvni) #přidání první neděle do slovníku, index nedělí bude chronologicky

    dt_prvni = time.strptime(str(prvni), "%Y-%m-%d") #rozdělení do slovníku
    #dt_posledni = time.strptime(str(pokus), "%Y-%m-%d")

    for x in range(1, 15): #přidávání týdnů k první neděli
        d1 = datetime.date(dt_prvni[0], dt_prvni[1], dt_prvni[2]) + datetime.timedelta(days=7*x) #připočítávej 7(dny) * x(týdnů)


        if d1 == devitnik(rok): #pokud je výsledek shodný s poslední počítanou nedělí, tak ho zformátuj, přidej do slovníku a vrat slovník
            #d11 = d1.strftime("%Y-%m-%d")
            #nedele.append(d11)

            return nedele
        else: #pokud není, tak poslední počítanou neděli jen přidej do slovníku a pokračuj
            d11 = d1.isoformat()
            nedele.append(d11)
