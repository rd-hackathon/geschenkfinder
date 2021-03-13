This project was created in the Relaxdays Code Challenge Vol. 1. See https://sites.google.com/relaxdays.de/hackathon-relaxdays/startseite for more information. Our participant IDs in the challenge were: CC-VOL1-68, CC-VOL1-??, CC-VOL1-??

# Geschenke Inspirator


## How to run this project
```bash
git clone https://github.com/rd-hackathon/geschenkfinder.git
cd geschenkfinder
docker build -t geschenkfinder . && docker run -p 8080:5000 geschenkfinder 
```

## Einschränkungen dieser Demo

*  Die Daten im Vorraus gecrawled und in eine Datenbank gequetscht.  In der Realität würde man natürlich auf einen aktuellen Datensatz zugreifen.
* Nicht zu jeder Kategorie, die Google erkennen kann, gibt es auch ein passendes Angebot. Insgesamt stehen nur 313 der ursprünglich 2296 Kategorien in Verbindung zu tatsächlich existierenden Artikeln.