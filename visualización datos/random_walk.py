#completado, con refactorización del ejercicio 15-5 incluída
from random import choice

class Randomwalk:
    """Una clase para generar caminos aleatorios."""
    
    def __init__(self, num_points=5000):
        """Inicializa los atributos de un camino."""
        self.num_points = num_points

        #Todos los caminos empiezan en (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calcula todos los puntos del camino."""

        #Sigue dando pasos hasta que el camino alcanza la longitud deseada.
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            #Rechaza los movimientos que no van a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue

            #Calcula la nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
            #Decide en qué dirección ir y cuánto avanzar en esa dirección.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            return x_direction * x_distance


            