import json

def get_stored_username():
    """Obtiene un nombre de usuario almacenado si está disponible."""
    filename = 'cap10\\username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Solicita un nuevo nombre de usuario."""
    username = input("What is your name? ")
    filename = 'cap10\\username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Saluda al usuario por su nombre."""
    username = get_stored_username()
    if username:
        while True:
            answer = input(f"Are you {username}? (y/n) ")
            if answer == 'y':
                print(f"Welcome back, {username}!")
                break
            elif answer == 'n':
                get_new_username()
                break
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()