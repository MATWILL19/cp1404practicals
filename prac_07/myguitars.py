"""Prac 07 Guitars program"""
from prac_07.guitar import Guitar

def main():
    print("My guitars!")
    guitars = load_guitars()
    guitars.sort()
    print("These are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {guitar.is_vintage()}")

def load_guitars():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars

def get_guitars():
    guitar_name = input("Name: ")
    guitars = []
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_details = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(guitar_details)
        print(f"{guitar_details.name} ({guitar_details.year}): ${guitar_details.cost} added.")
        guitar_name = input("Name: ")
    return guitars

main()