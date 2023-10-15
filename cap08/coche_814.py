def make_car(fabricante, modelo, **car_profile):
    """Crea un diccionario para un modelo particular de coche."""
    car_profile['fabricante'] = fabricante
    car_profile['modelo'] = modelo
    return car_profile

car_1 = make_car('peugeot', '208', color='blue', fuel='petrol')
car_2 = make_car('seat', 'leon fr', owner='mario', color='gray', size='XL')

print(car_1)
print(car_2)