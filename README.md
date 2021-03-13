This project was created in the Relaxdays Code Challenge Vol. 1. See https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite for more information. Our participant IDs in the challenge were: CC-VOL1-45, CC-VOL1-55, CC-VOL1-68

# Geschenke Inspirator

## Idee
Mit Google-Daten der zu beschenkenden Person und wahlweise zusätzlich noch mehr Datensätze weiterer Personen werden dort gespeicherte Interessen mit Kategorien von Relaxdays gematched, die dann auf Relaxdays Produkte verweisen. 

Die Google-Daten sind nicht im offiziellen Export vorhanden, stattdessen wird die Seite mit der personalisierten Werbung gespeichert und von diesem Inspirator verarbeitet: https://adssettings.google.com/authenticated?hl=de


## How to run this project

```bash
git clone https://github.com/rd-hackathon/geschenkfinder.git
cd geschenkfinder
docker build -t geschenkfinder . && docker run -p 8080:5000 geschenkfinder 
```

## Anmerkungen dieser Demo

* Die Daten im Vorraus gecrawled und in eine Datenbank gequetscht. In der Realität würde man natürlich auf einen aktuellen Datensatz zugreifen.
* Nicht zu jeder Kategorie, die Google erkennen kann, gibt es auch ein passendes Angebot. Insgesamt stehen nur 176 der ursprünglich 2296 Kategorien in Verbindung zu tatsächlich existierenden Artikeln.
* Man hätte natürlich auch gegen die bereits existierenden Kategorien von Relaxdays matchen können - durch die Suche haben wir uns eine leichte 'Fuzziness' versprochen :D
* Testdaten sind unter /testdaten zu finden. *user_A/B.html* sind 2 vollständige Nutzerprofile (wie sie von Google exportiert wurden), *2_kategorien.html* enthalten ungefähr genau 2 mögliche Kategorien und *keine_kategorien.html* enthält keine kompatible Kategorie.
* Es muss bei Google bereits einige Zeit die personalisierte Werbung angeschaltet sein, damit Google ein paar Kategorien zuweisen kann.
* Die Google-Export Seite muss auf deutsch gespeichert werden.