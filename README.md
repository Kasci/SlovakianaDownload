# Slovakiana Downloader

Tento skript je urceny na stahovanie snimiek z portalu Slovakiana.sk

## Prerequzita

Nainstalovany python3

## Pouzitie

Inicializacia a instalacia
```
pip install requests pillow
```
pripadne 
```
pip3 install requests pillow
```

Hned ku main.py je potrebne vytvorit subor s nazvom input.txt, kde je potrebne vlozit adresu stranky na slovakianu. Jedna adresa na riadok. Nie je potrebne ju ocistovat od parametrov za "?", ak tam nejake su.

Spustenie:
```
python main.py
```
alebo
```
python3 main.py
```

V konzole naskakuju upozornenia, ze je nie je vhodne ignorovat SLA certifikat, ale kedze Slovakiana nema ziaden validny, je jednoduchsie ho ignorovat.
