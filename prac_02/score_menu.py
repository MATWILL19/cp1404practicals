"""This program will get a score, show a result and print stars equal to score"""

MENU = """(I)nput Score
(P)rint result
(S)how stars
(Q)uit"""

def main(MENU):
    score = -1
    main_menu(MENU, score)
    print("Goodbye")

"""This function is the main menu of the program"""
def main_menu(MENU, score):
    print(MENU)
    menu_choice = input("")
    while menu_choice != "Q":
        if menu_choice == "I":
            score = int(input("Enter score: "))
        elif menu_choice == "P":
            result = calculate_score(score)
            print(result)
        elif menu_choice == "S":
            print_stars(score)
        print(MENU)
        menu_choice = input("")

"""This function calculates a result based on a given score"""
def calculate_score(score):
    if score > 100 or score < 0:
        result = "Invalid"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

"""This function prints the number of stars equal to a given password"""
def print_stars(score):
    for i in range(0, score):
        print("*", end="")
        print("")

main(MENU)