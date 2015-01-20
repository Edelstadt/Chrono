Chronologické pomůcky
=====================

Cíle
----

Cílem je vytvořit portovatelnou aplikaci, která bude sloužit jako pomůcka pro genealogy, archiváře a jiné nadšence pro historii.
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
