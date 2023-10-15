"""Un conjunto de clases que sirven para representar coches de gasolina y eléctricos."""

class Car:
    """Un simple intento de representar un coche."""

    def __init__(self, make, model, year):
        """Inicializa atributos para describir un coche"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo con un formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Imprime una frase que indica el kilometraje del coche."""
        print(f"This car has {self.odometer_reading} miles on it!")
    
    def update_odometer(self, mileage):
        """
        Establece la lectura del cuentakilómetros en el valor dado.
        Rechaza el cambio si intenta hacer retroceder el cunetakilómetros
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Suma la cantidad dada a la lectura del cuentakilómetros."""
        self.odometer_reading += miles
