#definimos la clase Dog. En Py,
#por convención, las clases van con primera mayus.
class Dog: 
    """Un simple intento de modelar un perro."""
    #una función que forma parte de una clase es un MÉTODO.
    #
    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simula un perro sentándose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simula hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")

#creamos una instancia de la clase Dog:
#my_dog como va en minus, sabemos que es una instancia.
#Dog va con mayus, sabemos que es una clase

my_dog = Dog('Argi', 5)
your_dog = Dog('Musgo', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()



