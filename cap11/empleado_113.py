class Empleado:
    """Crea un empleado."""

    def __init__(self, nombre, apellido, salario):
        """Inicializa Empleado."""
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    def dar_aumento(self, aumento=5_000):
        """Da un aumento salarial anual, p.d. 5.000 eur."""
        self.salario += aumento

# prueba = Empleado('pedro', 'martinez', 18000)
# prueba.dar_aumento(500)
# print(prueba.salario)