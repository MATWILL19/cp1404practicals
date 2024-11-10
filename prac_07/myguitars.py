"""Prac 07 Guitars program"""
from prac_07.guitar import Guitar

def main():
    print("My guitars!")
    guitars = get_guitars()
    print("These are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {guitar.is_vintage()}")

def get_guitars():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars

main()