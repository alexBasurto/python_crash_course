"""MÓDULO clases Admin y Permisos."""

from mod_usuario import Usuario

class Admin(Usuario):
    """Subclase admin, superclase usuario"""
    def __init__(self, nombre_usuario, apellidos_usuario, contraseña):
        """Inicializamos la clase admin."""
        super().__init__(nombre_usuario, apellidos_usuario, contraseña)
        self.permisos = Permisos()
    
class Permisos:
    """Representa los privilegios que tiene cualquier usuario admin."""
    def __init__(self):
        """Inicializa la clase."""
        self.permisos = ['puede añadir usuarios', 'puede borrar comentario', 'puede vetar usuarios']
    def show_permisos(self):
        """"Muestra los distintos permisos especiales de Administrador."""
        print("Permisos del usuario Administrador:")
        for permiso in self.permisos:
            print(f" - {permiso}")
