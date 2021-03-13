from bs4 import BeautifulSoup

useable = (
    "Blumen", "Comedy-Fernsehserien", "Computer und Elektronik", "Computerhardware", "Damenbekleidung", "Eltern", "Extremsportarten", "Fahrzeuge", "Fahrzeugkauf", "Familie", "Familienstand", "Fastfood", "Fernsehdramen", "Fernsehsender",
    "Film- und TV-Streaming", "Filmdramen", "Filme", "Filmkomödien", "Fitness", "Fußball", "Grußkarten", "Haarpflege", "Handys", "Haustiere", "Haustiernahrung und -pflegemittel", "Hochschulen und Universitäten", "Hotels und Unterkünfte",
    "Humor", "Hunde", "Kleidung", "Kochen und Rezepte", "Kosmetikartikel", "Kunstmuseen und -galerien", "Lauf- und Gehsport", "Luxusgüter", "Malerei", "Mode", "Musikindustrie", "Musikvideos", "Nachrichten", "Outdoor",
    "Reisen und Transport", "Restaurants", "Romantikfilme", "Schul- und Klassenzimmerbedarf", "Schwimmen", "Spielzeug", "Sport", "Weltmusik", "Wetter", "Zeitschriften", "Abendgarderobe", "Abenteuerreisen", "Abenteuerspiele",
    "Achtsamkeit und Meditation",
    "Alarmanlagen und Sicherheitssysteme", "American Football", "Angeln", "Anzüge, Kostüme und Businesskleidung", "Architektur", "Astronomie", "Audi", "Auto-Elektronik", "Auto-Leasing", "Autofinanzierung", "Automatenspiele",
    "Automobilausstellungen", "Automobilbranche", "Autorennsport", "Baby- und Kleinkindernährung", "Babys und Kleinkinder", "Bäckereien", "Backwaren", "Bade- und Körperpflegeprodukte", "Badezimmer", "Barbecue und Grillen",
    "Baseballausrüstung", "Basketball", "Basketballausrüstung", "Bauspielzeug", "Bekleidungsdienstleistungen", "BMX-Fahrräder", "Boxen", "Bräunungs- und Sonnenschutzprodukte", "Brettspiele", "Büro- und Computerschreibtische",
    "Büro- und Verwaltungsjobs",
    "Bürodienstleistungen", "Büromaterial", "Büromöbel", "Bürostühle", "Camcorder", "Cartoons", "Couch- und Beistelltische", "Cricketausrüstung", "Design", "Desserts", "Deutsche Küche", "Ehe", "Einzelsportarten", "Eislaufausrüstung",
    "Eislaufen", "Essen und Trinken", "Fahrräder und Zubehör", "Fahrradteile und -reparatur", "Fahrradzubehör", "Familie und Beziehungen", "Familienreisen", "Färbemittel", "Faser- und Textilkunst", "Fechten", "Feinkosthändler",
    "Fernsehgeräte", "Film- und Fernsehbranche", "Film- und Fernsehpreise", "Film- und Fernsehproduktion", "Filmfestivals", "Filmkritik und -vorschau", "Filmreferenzen", "Fisch und Meeresfrüchte", "Fitnessausrüstung und -zubehör",
    "Fitnessgeräte", "Fitnessstudios", "Foto- und Videoservices", "Freizeitkleidung", "Freizeitparks", "Freizeitschuhe", "Frühstückskomponenten", "Funkausrüstung", "Fußballausrüstung", "Garten- und Küchengrills", "Gartenarbeit",
    "Gartenbau", "Gartenmöbel",
    "Geschenkartikel", "Gesichts-Make-up", "Gesichtspflegeprodukte", "Getränke", "Gitarren", "Golf", "Golfausrüstung", "Gymnastik", "Gymnastikausrüstung", "Haarpflegeprodukte", "Halsketten", "Hand- und Körperseifen", "Handball",
    "Handrührgeräte", "Handtaschen und Geldbörsen", "Handwerk", "Haus und Garten", "Haushaltsgeräte", "Haushaltswaren", "Heimkinosysteme", "Heimwerken", "Herrenbekleidung", "Hochzeiten", "Hockey", "Hof- und Vorgartenpflege",
    "Holz und Kunststoffe", "Hosen und Shorts", "Hygiene- und Toilettenartikel", "Innenausstattung", "Kaffee", "Kaffee und Tee", "Kaffee- und Espressomaschinen", "Kalender- und Planungssoftware", "Kameraobjektive", "Kameras",
    "Kamine und Öfen", "Kampfkunst", "Kampfkunstausrüstung", "Kampfkunstfilme", "Kampfspiele", "Kampfsport", "Karriere und Beruf", "Karten", "Kartenspiele", "Käse", "Kegeln und Bowling", "Keramik und Töpferware",
    "Kfz-Werkstätten und -Wartung",
    "Kinder- und Spielzimmer", "Kinder- und Tiernamen", "Kinderbetreuung", "Kinderfahrräder", "Kleider", "Kleidungsaccessoires", "Kochboxen", "Kochgeschirr", "Kopfbedeckungen", "Kopfhörer", "Koreanische Küche", "Körperschmuck und -kunst",
    "Kosmetik- und Schönheitsexperten", "Kostüme", "Küche und Esszimmer", "Küchen- und Esszimmermöbel", "Küchengroßgeräte", "Küchenkleingeräte", "Küchenutensilien und -geräte", "Kühlschränke und Gefriertruhen",
    "Kunsterziehung (Bildende Künste und Design)", "Künstlerbedarf", "Lampen und Beleuchtung", "Laptops und Notebooks", "Lautsprecher", "Leichtathletik", "Leichtkrafträder", "Lernsoftware", "Lernspiele", "Liebe und Partnerschaft",
    "Mikrowellengeräte", "Möbelbau", "Museen", "Musikfilme", "Musikinstrumente", "Neujahr", "Nintendo", "Pferde", "Pizzerien", "Radfahrbekleidung", "Radfahren", "Reitausrüstung", "Rennräder", "Ringe", "Rucksäcke und Universaltaschen",
    "Saatgut und Samen", "Säfte", "Sammelkartenspiele", "Schilder", "Schlaf- und Badezimmer", "Schlafbekleidung", "Schlafzimmer", "Schuhe", "Skatebordausrüstung", "Smartphones", "Smartwatches", "Snacks", "Snowboardausrüstung",
    "Sofas und Sessel", "Softdrinks", "Sonnenbrillen", "Spaß und Quiz", "Spiele", "Spielsysteme und -konsolen", "Spielzeug für Babys und Kleinkinder", "Spielzeuge und Spiele für draußen", "Spielzeugmobile", "Sport-Training",
    "Sportandenken", "Sportartikel", "Sportbekleidung", "Sportergebnisse und -statistiken", "Sportfanausrüstung und -kleidung", "Sportgetränke", "Sportnachrichten", "Sportschuhe", "Standmixer und Entsafter", "Stiefel", "Strategiespiele",
    "Südamerikanische Küche", "Südasiatische Küche", "Südostasiatische Küche", "Suppen und Eintöpfe", "Surfen", "Süßigkeiten", "T-Shirts", "Tablet-PCs", "Tanzen", "Tee", "Tennis", "Tennisausrüstung", "Tierärzte", "Tiere", "Tiersportarten",
    "Tischspiele", "Tischtennis", "Tischtennisausrüstung", "Transport", "Türen und Fenster", "Uhren", "Unterwäsche", "Verpackung", "Visitenkarten und Büromaterial", "Vögel", "Volleyball", "Volleyballausrüstung", "Vorleger und Teppiche",
    "Wandern und Camping", "Wäscherei", "Waschmaschinen und Trockner", "Wasseraktivitäten", "Wasserfahrzeuge", "Wassersport", "Wassersportausrüstung", "Wildtiere", "Windeldienste, Windelzubehör und Sauberkeitserziehung", "Wintersport",
    "Wintersportausrüstung", "Wohnungsdekoration und Inneneinrichtung", "Wohnwagen und Wohnmobile", "Wohnzimmermöbel", "Wortspiele", "Wrestling", "Würfelspiele", "Zahnbürsten", "Zahnpasta", "Zeichnen und Malen", "Zeit und Kalender",
    "Zeitungen", "Zierfische und Aquarien", "Zirkus"
)


def parse_html(fh):
    set_categories = set()
    with open(fh, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        categories = soup.find('ul')
        for cat in categories.find_all('li'):
            if cat.text.strip() in useable:
                set_categories.add(cat.text.strip())
    return set_categories


if __name__ == '__main__':
    print(parse_html('user_A.html'))
