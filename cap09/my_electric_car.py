from car import Car, ElectricCar

my_volkswagen = Car('volkswagen', 'beetle', 1960)
print(my_volkswagen.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()