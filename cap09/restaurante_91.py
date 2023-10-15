class Restaurante:
    """Un simple intento de modelar un restaurante."""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre y tipo de cocina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        """Crea una descripción del restaurante."""
        print(f"El restaurante se llama {self.nombre_restaurante} y tiene una cocina de {self.tipo_cocina}.")
    
    def abrir_restaurante(self):
        """Indica que acaban de abrir el restaurante."""
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
    
restaurante = Restaurante('Los Argentinos', 'Horno de piedra')

print(f"Nombre: {restaurante.nombre_restaurante}.")
print(f"Tipo cocina: {restaurante.tipo_cocina}.")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()