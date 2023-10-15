class Restaurante:
    """Un simple intento de modelar un restaurante."""

    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de nombre y tipo de cocina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0

    def describir_restaurante(self):
        """Crea una descripción del restaurante."""
        print(f"El restaurante se llama {self.nombre_restaurante} y tiene una cocina de {self.tipo_cocina}.")
    
    def abrir_restaurante(self):
        """Indica que acaban de abrir el restaurante."""
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
    
    def establecer_numero_servido(self, comensales):
        """Establece de manera absoluta el número de clientes a los que se ha servido."""
        self.numero_servido = comensales
    
    def incrementar_numero_servido(self, comensales):
        """Incrementa el número de comensales servidos."""
        if comensales >= 0:
            self.numero_servido += comensales
        else:
            print("Lo sentimos, solo el administrador puede quitar comensales.")
    
restaurante = Restaurante('Los Argentinos', 'Horno de piedra')

print(f"Nombre: {restaurante.nombre_restaurante}.")
print(f"Tipo cocina: {restaurante.tipo_cocina}.")
print(f"Número de clientes servidos: {restaurante.numero_servido}.")
restaurante.numero_servido = 4
print(f"Número de clientes servidos: {restaurante.numero_servido}.")
restaurante.establecer_numero_servido(10)
print(f"Número de clientes servidos: {restaurante.numero_servido}.")
restaurante.incrementar_numero_servido(4)
print(f"Número de clientes servidos: {restaurante.numero_servido}.")
restaurante.incrementar_numero_servido(-8)
print(f"Número de clientes servidos: {restaurante.numero_servido}.")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()