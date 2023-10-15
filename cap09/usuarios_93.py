class Usuario:
    """Crea y da bienvenida al nuevo usuairo."""

    def __init__(self, nombre_usuario, apellidos_usuario, contraseña):
        """Inicializa la clase Usuarios."""
        self.nombre_usuario = nombre_usuario
        self.apellidos_usuario = apellidos_usuario
        self.contraseña = contraseña
    
    def describir_usuario(self):
        """Método que describe al usuario."""
        print(f"\nNombre usuario: {self.nombre_usuario} {self.apellidos_usuario}.")
        print(f"Contraseña: {self.contraseña}.")
    
    def saludar_usuario(self):
        """Método que saluda al usuario."""
        print(f"\nBienvenido, {self.nombre_usuario}.")

usuario_1 = Usuario('Lidia', 'Vivanco de Francisco', 'aph32443+')
usuario_2 = Usuario('Alex', 'Basurto Arana', 'pipi89')
usuario_3 = Usuario('Idoia Marina', 'Basurto Arana', 'cari1234')
usuario_4 = Usuario('Arturo', 'Basurto Arana', 'pesca_y_drones1987')

usuario_1.describir_usuario()
usuario_1.saludar_usuario()
usuario_2.describir_usuario()
usuario_2.saludar_usuario()
usuario_3.describir_usuario()
usuario_3.saludar_usuario()
usuario_4.describir_usuario()
usuario_4.saludar_usuario()