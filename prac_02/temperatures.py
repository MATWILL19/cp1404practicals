"""This program gets temperature and converts them to selected SI units"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius:c "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit:f "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

"""This function converts celsius to fahrenheit"""
def convert_celsius_to_fahrenheit(celsius):
    converted_fahrenheit = celsius * 9.0 / 5 + 32
    return converted_fahrenheit

""""This function converts fahrenheit to celsius"""
def convert_fahrenheit_to_celsius(fahrenheit):
    converted_celsius = (fahrenheit - 32) * 5 / 9
    return converted_celsius

main()

