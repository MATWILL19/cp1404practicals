"""CP1404 Practical 6 - Guitar"""
"""Estimated = 60m
Actual = m"""
from prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = get_guitars()
    print(f"{guitars}")

def get_guitars():
    guitars = []
    guitar_name = input("Name: ")
    guitar_year = int(input("Year: "))
    guitar_cost = float(input(": $"))
    guitars.append(guitar_name)
    guitars.append(guitar_year)
    guitars.append(guitar_cost)
    return guitars
main()

