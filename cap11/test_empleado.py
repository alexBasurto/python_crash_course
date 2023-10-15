import unittest
from empleado_113 import Empleado

class TestEmpleado(unittest.TestCase):
    """Pruebas para la clase Empleado."""

    def setUp(self):
        """Crea un empleado y su aumento."""
        self.empleado = Empleado('Alex', 'Basurto', 30_000)
        self.aumento = 3_000
        self.salario_final_1 = 35_000
        self.salario_final_2 = 33_000
    
    def test_dar_aumento_predeterminado(self):
        """Le da el aumento predeterminado."""
        self.empleado.dar_aumento()
        self.assertEqual(self.salario_final_1, self.empleado.salario)
    
    def test_dar_aumento_personalizado(self):
        """Le da un aumento personalizado."""
        self.empleado.dar_aumento(self.aumento)
        self.assertEqual(self.salario_final_2, self.empleado.salario)

if __name__ == '__main__':
    unittest.main()