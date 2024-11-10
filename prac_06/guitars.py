"""CP1404 Practical 6 - Guitar"""
"""Estimated = 60m
Actual = 1hr 10m"""
from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = get_guitars()
    print("These are my guitars:")
    max_name_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {guitar.is_vintage()}")


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


# def get_guitars_test():
#     guitar_name = "Gibson L-5 CES"
#     guitars = []
#     while guitar_name != "":
#         guitar_year = int(1922)
#         guitar_cost = float(16035.40)
#         guitar_details = Guitar(guitar_name, guitar_year, guitar_cost)
#         guitars.append(guitar_details)
#         print(f"{guitar_details.name} ({guitar_details.year}): ${guitar_details.cost} added.")
#         guitar_name = ""
#     guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
#     guitars.append(Guitar("Longest_guitar_there_ever_was_mate_you_shoulda_been_there", 2015, 1/2))
#     return guitars

main()

