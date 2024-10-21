"""
Wimbledon
Estimate: 60 minutes
Actual:   170 minutes
"""
FILENAME = "wimbledon.csv"

def main():
    """Display the wimbledon champions, there stats and the countries that have won wimbledon"""
    champions = get_wimbledon_file()
    champions_to_count, countries = process_wimbledon_champions(champions)
    display_results(champions_to_count, countries)

def process_wimbledon_champions(champions):
    """Process the champions and countries from champions list"""
    champion_to_count = {}
    countries = set()
    for champion in champions:
        countries.add(champion[1])
        try:
            champion_to_count[champion[2]] += 1
        except KeyError:
            champion_to_count[champion[2]] = 1
    return champion_to_count, countries

def get_wimbledon_file():
    """Read the attached wimbledon file and create champions list"""
    champions = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            champions.append(parts)
    return champions

def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))

main()

