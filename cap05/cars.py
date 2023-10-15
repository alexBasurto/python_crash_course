cars = ['audi', 'bmw', 'subaru', 'mg', 'toyota']

for car in cars:
    if car == 'bmw' or car == 'mg':
        print(car.upper())
    else:
        print(car.title())
