class Usuario:
    """Crea y da bienvenida al nuevo usuairo."""

    def __init__(self, nombre_usuario, apellidos_usuario, contraseña):
        """Inicializa la clase Usuarios."""
        self.nombre_usuario = nombre_usuario
        self.apellidos_usuario = apellidos_usuario
        self.contraseña = contraseña
        self.intentos_inicio = 0
    
    def describir_usuario(self):
        """Método que describe al usuario."""
        print(f"\nNombre usuario: {self.nombre_usuario} {self.apellidos_usuario}.")
        print(f"Contraseña: {self.contraseña}.")
    
    def saludar_usuario(self):
        """Método que saluda al usuario."""
        print(f"\nBienvenido, {self.nombre_usuario}.")

    def incrementar_intentos_inicio(self):
        """Incrementa en uno los intentos de inicio de sesión fallidos del usuario."""
        self.intentos_inicio += 1

    def restablecer_intentos_inicio(self):
        """Devuelve a cero los intentos de inicio de sesión fallidos."""
        self.intentos_inicio = 0

class Admin(Usuario):
    """Subclase admin, superclase usuario"""
    def __init__(self, nombre_usuario, apellidos_usuario, contraseña):
        """Inicializamos la clase admin."""
        super().__init__(nombre_usuario, apellidos_usuario, contraseña)
        self.permisos = ['puede añadir usuarios', 'puede borrar comentario', 'puede vetar usuarios']
    def show_permisos(self):
        print("Permisos del usuario Administrador:")
        for permiso in self.permisos:
            print(f" - {permiso}")



usuario_1 = Usuario('Lidia', 'Vivanco de Francisco', 'aph32443+')
usuario_2 = Usuario('Alex', 'Basurto Arana', 'pipi89')
usuario_3 = Usuario('Idoia Marina', 'Basurto Arana', 'cari1234')
usuario_4 = Usuario('Arturo', 'Basurto Arana', 'pesca_y_drones1987')
usuario_2.incrementar_intentos_inicio()
usuario_2.incrementar_intentos_inicio()
usuario_2.incrementar_intentos_inicio()
print(f"Los intentos de inicio de sesión fallidos del usuario 2 han sido {usuario_2.intentos_inicio}.")
usuario_2.restablecer_intentos_inicio()
print(f"Los intentos de inicio de sesión fallidos del usuario 2 han sido {usuario_2.intentos_inicio}.")

usuario_1.describir_usuario()
usuario_1.saludar_usuario()
usuario_2.describir_usuario()
usuario_2.saludar_usuario()
usuario_3.describir_usuario()
usuario_3.saludar_usuario()
usuario_4.describir_usuario()
usuario_4.saludar_usuario()

usuario_5 = Admin('Alex', 'Basurto Arana', 'ArgiJackRussell2018')
usuario_5.describir_usuario()
usuario_5.saludar_usuario()
usuario_5.show_permisos()