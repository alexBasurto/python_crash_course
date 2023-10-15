from random import choice

numeros_candidatos = list(range(0, 99_999))
#numeros_premiados = []
mi_numero = 35_698
veces = 0

while True:
    premiado = choice(numeros_candidatos)
    veces += 1
    if premiado == mi_numero:
        print(f"Su número, el {mi_numero} ha resultado ganador! Para ello ha tenido que participar {veces} veces.")
        break
