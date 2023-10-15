def greet_users(names):
    """Imprime un saludo sencillo para cada usuario de la lista."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)