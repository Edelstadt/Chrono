#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Usage:
    CLI.py slunecniKruh <rok>
    CLI.py konkurenty <rok>
    CLI.py nedelni_pismeno_j <rok>
    CLI.py nedelni_pismeno_g <rok>
    CLI.py zlate_cislo <rok>
    CLI.py epakta_g <rok>
    CLI.py epakta_j <rok>
    CLI.py velikonoce_j <rok>
    CLI.py velikonoce_g <rok>
    CLI.py devitnik <rok>
    CLI.py misericordia <rok>
    CLI.py nedele_po_devitniku <rok>
    CLI.py nedele_masopustni <rok>
    CLI.py popelecni_streda <rok>
    CLI.py prazna_nedele <rok>
    CLI.py druha_postni_nedele <rok>
    CLI.py kychava_nedele <rok>
    CLI.py druzebna_nedele <rok>
    CLI.py smrtna_nedele <rok>
    CLI.py kvetna_nedele <rok>
    CLI.py zeleny_ctvrtek <rok>
    CLI.py velky_patek <rok>
    CLI.py bila_sobota <rok>
    CLI.py bila_nedele <rok>
    CLI.py den_svatosti <rok>
    CLI.py jubilate <rok>
    CLI.py cantate <rok>
    CLI.py krizova_nedele <rok>
    CLI.py nanebevstoupeni <rok>
    CLI.py exaudi <rok>
    CLI.py letnice <rok>
    CLI.py trojice <rok>
    CLI.py boziho_tela <rok>
    CLI.py treti_nedele_ad <rok>
    CLI.py ctvrta_nedele_ad <rok>
    CLI.py druha_nedele_ad <rok>
    CLI.py prvni_nedele_ad <rok>
    CLI.py letni_nedele <rok>
    CLI.py masopustni_nedele <rok>
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import time
from docopt import docopt
from funkce import slunecni_kruh, konkurenty, zlate_cislo, epakta_g, epakty_j
from funkce import devitnik, misericordia, ctvrta_ned_ad
from funkce import nedelni_pismeno_j, nedelni_pismeno_g, velikonoce_j
from funkce import velikonoce_g, nedele_po_devitniku, masopustni_nedele
from funkce import popelecni_streda, prazna_nedele, druha_postni
from funkce import kychava_nedele, druzebna_nedele, smrtna_nedele
from funkce import kvetna_nedele, zeleny_ctvrtek, velky_patek
from funkce import bila_sobota, bila_nedele, den_svatosti, jubilate
from funkce import cantate, krizova_nedele, nanebevstoupeni, exaudi
from funkce import letnice, trojice, boziho_tela, treti_ned_ad
from funkce import druha_ned_ad, prvni_ned_ad, nedele_letni
from funkce import masopust

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Chrono 0.1')
    rok = int(arguments['<rok>'])
    sk = arguments['slunecniKruh']
    konkurenty = arguments['konkurenty']
    ned_p_j = arguments['nedelni_pismeno_j']
    ned_p_g = arguments['nedelni_pismeno_g']
    zla_cis = arguments['zlate_cislo']
    epak_j = arguments['epakta_j']
    epak_g = arguments['epakta_g']
    velik_j = arguments['velikonoce_j']
    velik_g = arguments['velikonoce_g']
    devit = arguments['devitnik']
    miseri = arguments['misericordia']
    ned_po_dev = arguments['nedele_po_devitniku']
    ned_mas = arguments['nedele_masopustni']
    pop_str = arguments['popelecni_streda']
    praz_ned = arguments['prazna_nedele']
    druh_po_ned = arguments['druha_postni_nedele']
    kych_ned = arguments['kychava_nedele']
    druz_ned = arguments['druzebna_nedele']
    smrt_ned = arguments['smrtna_nedele']
    kvet_ned = arguments['kvetna_nedele']
    zel_ctv = arguments['zeleny_ctvrtek']
    vel_pat = arguments['velky_patek']
    bil_sob = arguments['bila_sobota']
    bil_ned = arguments['bila_nedele']
    den_svat = arguments['den_svatosti']
    jub = arguments['jubilate']
    cant = arguments['cantate']
    kriz_ned = arguments['krizova_nedele']
    naneb = arguments['nanebevstoupeni']
    exa = arguments['exaudi']
    let = arguments['letnice']
    troj = arguments['trojice']
    boz_tel = arguments['boziho_tela']
    p_ned_ad = arguments['prvni_nedele_ad']
    d_ned_ad = arguments['druha_nedele_ad']
    t_ned_ad = arguments['treti_nedele_ad']
    c_ned_ad = arguments['ctvrta_nedele_ad']
    let_ned = arguments['letni_nedele']
    mas_ned = arguments['masopustni_nedele']
    if sk:
        print(slunecni_kruh(rok))
    if konkurenty:
        print(konkurenty(rok))
    if ned_p_j:
        print(nedelni_pismeno_j(slunecni_kruh(rok)))
    if ned_p_g:
        print(nedelni_pismeno_g(nedelni_pismeno_j(slunecni_kruh(rok)), rok))
    if zla_cis:
        print(zlate_cislo(rok))
    if epak_g:
        print(epakta_g(rok))
    if epak_j:
        print(epakty_j(zlate_cislo(rok)))
    if velik_j:
        print(time.strftime("%Y %d.%m", velikonoce_j(rok)))
    if velik_g:
        print(time.strftime("%Y %d.%m", velikonoce_g(rok)))
    if devit:
        print(time.strftime("%Y %d.%m", devitnik(rok)))
    if miseri:
        print(time.strftime("%Y %d.%m", misericordia(rok)))
    if ned_po_dev:
        print(time.strftime("%Y %d.%m", nedele_po_devitniku(rok)))
    if ned_mas:
        print(time.strftime("%Y %d.%m", masopustni_nedele(rok)))
    if pop_str:
        print(time.strftime("%Y %d.%m", popelecni_streda(rok)))
    if praz_ned:
        print(time.strftime("%Y %d.%m", prazna_nedele(rok)))
    if druh_po_ned:
        print(time.strftime("%Y %d.%m", druha_postni(rok)))
    if kych_ned:
        print(time.strftime("%Y %d.%m", kychava_nedele(rok)))
    if druz_ned:
        print(time.strftime("%Y %d.%m", druzebna_nedele(rok)))
    if smrt_ned:
        print(time.strftime("%Y %d.%m", smrtna_nedele(rok)))
    if kvet_ned:
        print(time.strftime("%Y %d.%m", kvetna_nedele(rok)))
    if zel_ctv:
        print(time.strftime("%Y %d.%m", zeleny_ctvrtek(rok)))
    if vel_pat:
        print(time.strftime("%Y %d.%m", velky_patek(rok)))
    if bil_sob:
        print(time.strftime("%Y %d.%m", bila_sobota(rok)))
    if bil_ned:
        print(time.strftime("%Y %d.%m", bila_nedele(rok)))
    if den_svat:
        print(time.strftime("%Y %d.%m", den_svatosti(rok)))
    if jub:
        print(time.strftime("%Y %d.%m", jubilate(rok)))
    if cant:
        print(time.strftime("%Y %d.%m", cantate(rok)))
    if kriz_ned:
        print(time.strftime("%Y %d.%m", krizova_nedele(rok)))
    if naneb:
        print(time.strftime("%Y %d.%m", nanebevstoupeni(rok)))
    if exa:
        print(time.strftime("%Y %d.%m", exaudi(rok)))
    if let:
        print(time.strftime("%Y %d.%m", letnice(rok)))
    if troj:
        print(time.strftime("%Y %d.%m", trojice(rok)))
    if boz_tel:
        print(time.strftime("%Y %d.%m", boziho_tela(rok)))
    if p_ned_ad:
        print(time.strftime("%Y %d.%m", prvni_ned_ad(rok)))
    if d_ned_ad:
        print(time.strftime("%Y %d.%m", druha_ned_ad(rok)))
    if t_ned_ad:
        print(time.strftime("%Y %d.%m", treti_ned_ad(rok)))
    if c_ned_ad:
        print(time.strftime("%Y %d.%m", ctvrta_ned_ad(rok)))
    if let_ned:
        x = nedele_letni(rok)
        for a, v in enumerate(x):
            print(str(v[0]), " ", str(v[2]) ,"." ,str(v[1]), sep="")
    if mas_ned:
        x = masopust(rok)
        for a, v in enumerate(x):
            print(str(v[0]), " ", str(v[2]), ".", str(v[1]), sep="")
