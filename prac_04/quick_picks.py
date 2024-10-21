import random
MAXIMUM_NUMBER = 45
MINIMUM_NUMBER = 1
NUMBERS_PER_LINE = 6

def main():
    """Generate 6 quick picks on a number of lines inputted"""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_picks = quick_pick_generator()
        print(" ".join(f"{quick_pick:2}" for quick_pick in quick_picks))

def quick_pick_generator():
    """Generate quick picks from a given number"""
    quick_picks = []
    for number in range(NUMBERS_PER_LINE):
        quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while quick_pick in quick_picks:
            quick_pick = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_picks.append(quick_pick)
    quick_picks.sort()
    return quick_picks

main()