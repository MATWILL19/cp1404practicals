"""Taxi simulator program"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Simulate a taxi company"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100 ,2)
        , SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("let's drive!")
    bill = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis)
            current_taxi.start_fare()
        elif choice == "D":
            if current_taxi is None:
                print("You must choose a taxi!")
            else:
               bill = drive(current_taxi, bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: {bill}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)


def choose_taxi(taxis):
    """Get user taxi choice"""
    print("Taxi's available:")
    for i, taxi in enumerate(taxis):
        print(i, taxi)
    taxis_length = len(taxis)
    taxi_choice = get_integer(taxis_length)
    return taxis[taxi_choice]

def drive(current_taxi, bill):
    """Simulate taxi driving and return a bill"""
    drive_distance = int(input("Drive how far? "))
    current_taxi.drive(drive_distance)
    current_fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} will cost you ${current_fare}")
    return bill + current_fare

def get_integer(taxis_length):
    """Error check integer inputs"""
    while True:
        try:
            integer_input = int(input(">>> "))
            while integer_input < 0 or integer_input > taxis_length - 1:
                print("Invalid taxi choice")
                integer_input = int(input(">>> "))
            return integer_input
        except ValueError:
            print("Invalid input; enter a valid number")

main()