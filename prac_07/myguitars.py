"""Prac 07 Guitars program"""
from prac_07.guitar import Guitar

def main():
    print("My guitars!")
    guitars = load_guitars()
    get_guitars(guitars)
    guitars.sort()
    save_guitars(guitars)
    print("These are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {guitar.is_vintage()}")

def load_guitars():
    """Load guitars from file and append to guitars list"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars

def get_guitars(guitars):
    """Get guitars from user input and append to guitars list."""
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_details = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_details)
        print(f"{guitar_details.name} ({guitar_details.year}): ${guitar_details.cost} added.")
        guitar_name = input("Name: ")
    return guitars

def save_guitars(guitars):
    """Save guitars list to file"""
    save_guitars = []
    for guitar in guitars:
        parts_0 = [guitar.name, str(guitar.year), str(guitar.cost)]
        parts_1 = ",".join(parts_0)
        save_guitars.append(parts_1)
    with open(f"{'guitars.csv'}", "w") as out_file:
        for guitar in save_guitars:
            out_file.write(guitar + "\n")
    return

main()