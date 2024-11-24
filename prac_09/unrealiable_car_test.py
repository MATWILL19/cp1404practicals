from prac_09.unreliable_car import Unreliablecar

my_shitbox = Unreliablecar("Astra 2003", 120, 30)
my_baby = Unreliablecar("Sonata 2022", 120, 90)
for i in range(0, 3):
    print(f"{my_shitbox.name} drove {my_shitbox.drive(40)} and has {my_shitbox.fuel} fuel left")
    print(f"{my_baby.name} drove {my_baby.drive(40)} and has {my_baby.fuel} fuel left")
