"""This program will determine a result based on a score"""
import random

def main():
    score = float(input("Enter score: "))
    result = calculate_score(score)
    print(result)
    score = random.randint(0, 100)
    result = calculate_score(score)
    print(score)
    print(result)

"""This function will calculate the result"""
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

main()

