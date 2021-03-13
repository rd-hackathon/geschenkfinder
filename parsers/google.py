from bs4 import BeautifulSoup

useable = (
    'Blumen', 'Computer und Elektronik', 'Eltern', 'Fahrzeuge', 'Familie', 'Filme', 'Fitness', 'Fußball', 'Grußkarten', 'Haarpflege', 'Handys', 'Haustiere', 'Hochschulen und Universitäten', 'Hotels und Unterkünfte', 'Humor', 'Hunde',
    'Kleidung', 'Kochen und Rezepte', 'Kosmetikartikel', 'Malerei', 'Mode', 'Nachrichten', 'Outdoor', 'Reisen und Transport', 'Restaurants', 'Schwimmen', 'Spielzeug', 'Sport', 'Wetter', 'Zeitschriften', 'Abendgarderobe',
    'American Football', 'Angeln', 'Architektur', 'Auto-Elektronik', 'Babys und Kleinkinder', 'Bäckereien', 'Backwaren', 'Badezimmer', 'Barbecue und Grillen', 'Basketball', 'Bauspielzeug', 'BMX-Fahrräder', 'Boxen', 'Brettspiele',
    'Büro- und Computerschreibtische', 'Büromaterial', 'Büromöbel', 'Bürostühle', 'Cartoons', 'Couch- und Beistelltische', 'Design', 'Desserts', 'Deutsche Küche', 'Ehe', 'Essen und Trinken', 'Fahrräder und Zubehör', 'Fahrradzubehör',
    'Familie und Beziehungen', 'Fernsehgeräte', 'Fisch und Meeresfrüchte', 'Fitnessgeräte', 'Fitnessstudios', 'Gartenarbeit', 'Gartenmöbel', 'Gesichts-Make-up', 'Getränke', 'Gitarren', 'Golf', 'Gymnastik', 'Halsketten', 'Handball',
    'Handtaschen und Geldbörsen', 'Handwerk', 'Haus und Garten', 'Haushaltsgeräte', 'Haushaltswaren', 'Heimwerken', 'Hochzeiten', 'Hockey', 'Holz und Kunststoffe', 'Hosen und Shorts', 'Innenausstattung', 'Kaffee', 'Kaffee und Tee',
    'Kaffee- und Espressomaschinen', 'Kameras', 'Kamine und Öfen', 'Karriere und Beruf', 'Karten', 'Kartenspiele', 'Käse', 'Kegeln und Bowling', 'Kfz-Werkstätten und -Wartung', 'Kinder- und Spielzimmer', 'Kinderfahrräder', 'Kleider',
    'Kochgeschirr', 'Kopfbedeckungen', 'Kopfhörer', 'Koreanische Küche', 'Kostüme', 'Küche und Esszimmer', 'Küchen- und Esszimmermöbel', 'Küchenkleingeräte', 'Küchenutensilien und -geräte', 'Kühlschränke und Gefriertruhen',
    'Künstlerbedarf', 'Lampen und Beleuchtung', 'Laptops und Notebooks', 'Lautsprecher', 'Leichtathletik', 'Lernspiele', 'Möbelbau', 'Musikinstrumente', 'Pferde', 'Pizzerien', 'Radfahren', 'Rennräder', 'Ringe', 'Saatgut und Samen', 'Säfte',
    'Schilder', 'Schlaf- und Badezimmer', 'Schlafzimmer', 'Schuhe', 'Smartphones', 'Snacks', 'Sofas und Sessel', 'Softdrinks', 'Sonnenbrillen', 'Spiele', 'Spielzeug für Babys und Kleinkinder', 'Spielzeuge und Spiele für draußen',
    'Sport-Training', 'Sportartikel', 'Sportschuhe', 'Stiefel', 'Strategiespiele', 'Suppen und Eintöpfe', 'Surfen', 'Süßigkeiten', 'T-Shirts', 'Tablet-PCs', 'Tanzen', 'Tee', 'Tennis', 'Tierärzte', 'Tiere', 'Tischspiele', 'Tischtennis',
    'Tischtennisausrüstung', 'Transport', 'Türen und Fenster', 'Uhren', 'Unterwäsche', 'Verpackung', 'Visitenkarten und Büromaterial', 'Vögel', 'Volleyball', 'Vorleger und Teppiche', 'Wandern und Camping', 'Waschmaschinen und Trockner',
    'Wassersport', 'Wildtiere', 'Wintersport', 'Wohnwagen und Wohnmobile', 'Wohnzimmermöbel', 'Würfelspiele', 'Zahnbürsten', 'Zahnpasta', 'Zeichnen und Malen', 'Zeit und Kalender', 'Zeitungen', 'Zierfische und Aquarien', 'Zirkus'
)


def parse_html(fh):
    set_categories = set()
    with open(fh, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        categories = soup.find('ul')
        for cat in categories.find_all('li'):
            if cat.text.strip() in useable:
                set_categories.add(cat.text.strip())
    return set_categories


if __name__ == '__main__':
    print(parse_html('user_A.html'))
