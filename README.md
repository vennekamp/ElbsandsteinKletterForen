# Ein paar Scripte zum Vergleich der Sandsteinforen:
## Die Dateien
### __"fetch..."__ 
sind Skripte zum Laden der Foren (es fehlt aber alles außer SBB)
### __"Link_SBB2.....py"__ 
sind Skripte zur Korrelation der Wege aus den verschiedenen Foren (Der eigentliche Vergleich und die eigentliche Zuordnung)
### __"create_web_server_and_pages"__ 
enthält __"summit_corr.py":__ Das Skript zur Abfrage der SQL-Tabellen und starten eines 'bottle.py' Webservers.

## Nutzung

__'create_web_server_and_pages\summit_corr.py'__ starten und in einem Webbrowser eine lokale Seite laden in Form 'http://127.0.0.1:5050/summit/[Gipfel]>[minimaleÜbereinstimmung]'.

Beispiele:
- [http://127.0.0.1:5050/summit/Sonny>85](https://github.com/vennekamp/ElbsandsteinKletterForen/blob/master/S%C3%BCdwestliche%20Zinne_100.htm)
- [http://127.0.0.1:5050/summit/Falkenstein>85](https://github.com/vennekamp/ElbsandsteinKletterForen/blob/master/S%C3%BCdwestliche%20Zinne_24.htm)
- [http://127.0.0.1:5050/summit/Gro%C3%9Fer%20Gl%C3%BCcksturm](https://github.com/vennekamp/ElbsandsteinKletterForen/blob/master/Gro%C3%9Fer%20Gl%C3%BCcksturm_70.htm)

Reihenfolge der Zeilen und Zuordnungen innerhalb der Zeile könenn per DRAG `n DROP verändert werden.

## Offene Punkte
- Zuordnung als 'OK' markieren / ausblenden
- Speicherung einer neuen Zuordnung in der Datenbank
- Editieren von Texten
- ....




