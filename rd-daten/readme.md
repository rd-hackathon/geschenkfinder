Die einzige wirklich interessante Datei ist *daten.db*: Darin sind die Produkte der 176 gecrawlten Kategorien.

**Andere Dateien:**
* *crawler_relaxdays.py*: Hat die Daten in die Datenbank geschrieben. (Extra Module werden benötigt, sind aber nicht in der requirements.txt/Dockerfile, da streng genommen nicht relevanter Teil des Projekts)
* *alle_google_kategorien.txt*: 2296 Kategorien, die Google einer Person zuweisen kann. (Oder zumindest die, die Google uns verraten hat.)
* *handgefilterte_kategorien.txt*: 500 verbliebene Kategorien, wo der größte Datenmüll aussortiert wurde (sprich Dinge, zu denen Relaxdays vermutlich keine Produkte führt, zum Beispiel "South Carolina (nördliche Region)")
* *bereignete_kategorien.txt*: 317 verbliebene Kategorien, zu denen Relaxdays etwas gefunden hat ODER Vorschläge gemacht hat (Wusstet ihr schon, dass man bei der Suche nach "Nintendo" ein Insektenhaus vorgeschlagen bekommt? Ist das ein Bug?🐞)
* *daten_old_and_fuzzier.db*: enthält diese 317 Kategorien. Wir haben uns dagegen entschieden, die Vorschläge zu nutzen, weil sie doch meist relativ zusammenhangslos waren.
* *working.txt*: 176 Kategorien, die auch in der daten.db drin sind.
* *broken.txt*: die anderen 137 Kategorien, zu denen Relaxdays Vorschläge liefert. ("Kampfkunstfilme" liefert zum Beispiel Hüpftier Einhörner... das wäre ein Film, an dem ich interessiert wäre 🎥)
