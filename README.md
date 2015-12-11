Chronological tools
=====================

Goals
----

The aim is to create a ported application that will serve as a tool for genealogists, archivists and other enthusiasts of history primarily for the Czech environment (if you want to Czech countries).
You should be able to restate historical dating, calculate religious holidays such as Easter, etc., and it is mostly the older data (usability, at least for the years 1500+ - not necessary to calculate YEARS 1300 AND BELOW)

The first attempt to put it into practice
[Link] (http://edelstadt.pythonanywhere.com/)

Applications should be not only as an Internet application, but also as an application for a win, linux and perhaps for android

Option 1 - portable js, which could be theoretically run anywhere. The idea is - to create a file (probably xml?), Where they will be registered all required years and have listed holidays (basically say about 700-year calendar). The user enters into html pages only a year and generates js "calendar" for a given year, which will be listed holidays (which will be loaded from the aforementioned xml files). Superstructure would have been searches by years of known data, ie. Eg. By the famous golden number, competitors and epakty search for the relevant years.

Option 2 - funkce.py to create cross-platform GUI. Probably easier solution, but in practice probably impractical (it certainly would not be as portable as html with js)

For both options must tweak funkce.py (for Option 1 as a tool for generating data for Option 2 for the actual calculations)

USAGE:
=====

```python
import funkce

year = 2016
print(funkce.slunecni_kruh(year))
print(funkce.nedelni_pismeno_j(funkce.slunecni_kruh(year)))
print(funkce.konkurenty(year))
print(funkce.zlate_cislo(year))
print(funkce.epakty_j(funkce.zlate_cislo(year)))
print(funkce.epakta_g(year))
print(funkce.nedelni_pismeno_g(funkce.nedelni_pismeno_j(funkce.slunecni_kruh(year)), year))
# next return timetuple
print(funkce.velikonoce_j(year))  
print(funkce.velikonoce_g(year))
print(funkce.devitnik(year))
print(funkce.nedele_po_devitniku(year))
print(funkce.masopustni_nedele(year))
print(funkce.popelecni_streda(year))
print(funkce.prazna_nedele(year))
print(funkce.druha_postni(year))
print(funkce.kychava_nedele(year))
print(funkce.druzebna_nedele(year))
print(funkce.smrtna_nedele(year))
print(funkce.kvetna_nedele(year))
print(funkce.zeleny_ctvrtek(year))
print(funkce.velky_patek(year))
print(funkce.bila_sobota(year))
print(funkce.bila_nedele(year))
print(funkce.den_svatosti(year))
print(funkce.misericordia(year))
print(funkce.jubilate(year))
print(funkce.exaudi(year))
print(funkce.letnice(year))
print(funkce.trojice(year))
print(funkce.boziho_tela(year))
print(funkce.ctvrta_ned_ad(year))
print(funkce.treti_ned_ad(year))
print(funkce.druha_ned_ad(year))
print(funkce.prvni_ned_ad(year))
# return list timetuple
print(funkce.masopust(year))
print(funkce.nedele_letni(year))
```
Chronologické pomůcky
=====================

Cíle
----

Cílem je vytvořit portovatelnou aplikaci, která bude sloužit jako pomůcka pro genealogy, archiváře a jiné nadšence pro historii primárně pro české prostředí (chcete-li, pro České země).
Měla by umět přepočítávat historické datace, počítat církevní svátky jako velikonoce atd. a to hlavně a především pro starší data (použitelnost alespoň pro roky 1500+ - NENÍ NUTNÉ POČÍTAT S ROKY 1300 A MÉNĚ)

První pokus o převedení do praxe
[Link](http://edelstadt.pythonanywhere.com/)

Aplikace by měla být nejen jako internetová aplikace, ale i jako aplikace pro win, linux a snad i pro android

Varianta 1 - přenositelný js, který by bylo možno spouštět teoreticky kdekoli. Myšlenka je taková - vytvořit soubor (nejspíš xml?), kde budou zapsané všechny požadované roky a v nich vypsané svátky (v podstatě řekněme cca 700letý kalendář). Uživatel zadá do html stránky pouze rok a js vygeneruje "kalendář" pro zadaný rok, kde budou vypsány svátky (které budou nataženy z již zmíněných xml souborů). Nadstavba by byla vyhledávání roků podle známých údajů, tj. např. podle známého zlatého čísla, konkurenty a epakty vyhledat odpovídající roky.

Varianta 2 - pro funkce.py vytvořit přenositelné GUI. Pravděpodobně jednodušší řešení, nicméně v praxi nejspíš neproveditelné (rozhodně by to nebylo tak přenositelné jako html s js)

Pro obě varianty nutno vyladit funkce.py (pro variantu 1 jako nástroj pro vygenerování dat, pro variantu 2 pro samotné výpočty)


Testy
-----

```python -m unitest discover```
