
COLOUR_NAME_TO_CODE = {"absolute zero": "#0048ba", "alizarin crimson": "#e32636", "amethyst": "#9966cc",
                       "prussian blue": "003153", "plum": "#8e4585", "timberwolf":"#dbd7d2", "up forest green": "#014421",
                       "ultramarine": "#3f00ff", "imperial red": "#ed2939", "japanese carmine": "#9d2933"}

print(COLOUR_NAME_TO_CODE)
colour_choice = input("Enter a colour: ").lower()
while colour_choice != "":
    try:
        print(f"{colour_choice} is {COLOUR_NAME_TO_CODE[colour_choice]}")
    except KeyError:
        print("Invalid colour")
    colour_choice = input("Enter a colour: ").lower()
