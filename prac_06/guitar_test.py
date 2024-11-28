from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
my_guitar = Guitar("Foundoutback", 2015, 56.50)
print(f"Gibson get_age() - Expected 100. Got {gibson.get_age()}")
print(f"my_guitar get_age() - Expected 100. Got {my_guitar.get_age()}")
print(f"gibson is_vintage( - Expected True. Got {gibson.is_vintage()}")
print(f"my_guitar is_vintage( - Expected False. Got {my_guitar.is_vintage()}")