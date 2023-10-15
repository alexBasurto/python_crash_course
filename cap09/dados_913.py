from random import randint

class Dados:
    """Intento de recrear el comportamiento de un dado."""

    def __init__(self, caras=6):
        """Inicializa el dado y define el número de caras."""
        self.caras = caras
    
    def tirar_dado(self):
        """Tira el dado."""
        return randint(1, self.caras)

dado_parchis = Dados(6)

print(f"\nTiramos el dado de parchis, de {dado_parchis.caras} caras...")
veces = 0
while veces < 10:
    print(dado_parchis.tirar_dado())
    veces += 1

dado_rpg = Dados(10)
dado_dnd = Dados(20)

print(f"\nTiramos el dado de RPG, de {dado_rpg.caras} caras...")
veces = 0
while veces < 10:
    print(dado_rpg.tirar_dado())
    veces += 1

print(f"\nTiramos el dado de Dragones y Mazmorras, de {dado_dnd.caras} caras...")
veces = 0
while veces < 10:
    print(dado_dnd.tirar_dado())
    veces += 1