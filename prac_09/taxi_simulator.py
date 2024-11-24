"""Taxi simulator program"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Simulate a taxi company"""
    current_taxi = None
    print("let's drive!")
    print(MENU)
    choice = input(">>> ")
    while choice != "Q"
        if choice == "C"
            choose_taxi()

def choose_taxi():
    """Get user taxi choice"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100 ,2)
        , SilverServiceTaxi("Hummer", 200, 4)]

def drive():
    """Simulate taxi driving and return a bill"""

main()