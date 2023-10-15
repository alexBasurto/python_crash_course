import json

def get_numero_favorito():
    """Obtiene el número favorito si está disponible."""
    filename = 'cap10\\num_favorito.json'
    try:
        with open(filename) as f:
            numero_favorito = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return numero_favorito

def new_numero_favorito():
    """Solicita un nuevo número favorito."""
    numero_favorito = input("\nPor favor, introduzca su número favorito: ")
    filename = 'cap10\\num_favorito.json'
    with open(filename, 'w') as f:
        json.dump(numero_favorito, f)
    return numero_favorito

def numero_favorito():
    """Facilita el número favorito del usuario."""
    numero_favorito = get_numero_favorito()
    if numero_favorito:
        print(f"\nTu número favorito es el {numero_favorito}!")
    else:
        numero_favorito = new_numero_favorito()
        print(f"\nRecordaré tu número favorito la próxima vez.")


numero_favorito()
