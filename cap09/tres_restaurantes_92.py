class Restaurante:
    """Un simple intento de modelar un restaurante."""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre y tipo de cocina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        """Crea una descripción del restaurante."""
        print(f"El restaurante se llama {self.nombre_restaurante} y su cocina es de {self.tipo_cocina}.")
    
    def abrir_restaurante(self):
        """Indica que acaban de abrir el restaurante."""
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
    
restaurante1 = Restaurante('Los Argentinos', 'Pizzería con horno de piedra')
restaurante2 = Restaurante('Coppola', 'Italiano')
restaurante3 = Restaurante('Aritza', 'Cocina tradicional vasca')

print(f"\nNombre: {restaurante1.nombre_restaurante}.")
print(f"Tipo cocina: {restaurante1.tipo_cocina}.")
restaurante1.describir_restaurante()
restaurante1.abrir_restaurante()

print(f"\nNombre: {restaurante2.nombre_restaurante}.")
print(f"Tipo cocina: {restaurante2.tipo_cocina}.")
restaurante2.describir_restaurante()
restaurante2.abrir_restaurante()

print(f"\nNombre: {restaurante3.nombre_restaurante}.")
print(f"Tipo cocina: {restaurante3.tipo_cocina}.")
restaurante3.describir_restaurante()
restaurante3.abrir_restaurante()