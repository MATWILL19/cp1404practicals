from prac_09.taxi import Taxi

my_taxi= Taxi("Prius 1", 100)
my_taxi.start_fare()
my_taxi.drive(40)
print(f"{my_taxi.name} has {my_taxi.fuel} fuel left, drove {my_taxi.current_fare_distance}, current fair is: {my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"{my_taxi.name} has {my_taxi.fuel} fuel left, drove {my_taxi.current_fare_distance}, current fair is: {my_taxi.get_fare()}")