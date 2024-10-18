"""This program will get a score, show a result and print stars equal to score"""

MENU = """(I)nput Score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    score = get_score()
    main_menu(score)
    print("Goodbye")

"""This function is the main menu of the program"""
def main_menu(score):
    print(MENU)
    menu_choice = input("").upper()
    while menu_choice != "Q":
        if menu_choice == "I":
            score = get_score()
        elif menu_choice == "P":
            result = calculate_score(score)
            print(result)
        elif menu_choice == "S":
            print_stars(score)
        print(MENU)
        menu_choice = input("").upper()

"""This function calculates a result based on a given score"""
def calculate_score(score):
    if score >= 90:
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

"""This function gets and error checks a score"""
def get_score():
    score = int(input("Enter score: "))
    while score > 100 or score < 0:
        print("Invalid")
        score = int(input("Enter score: "))
    return score

main()