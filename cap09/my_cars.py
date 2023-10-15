from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'golf', 2001)
print(my_beetle.get_descriptive_name())

my_prius = EC('toyota', 'prius', 2013)
print(my_prius.get_descriptive_name())