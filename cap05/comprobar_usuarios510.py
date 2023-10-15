current_users = ['jaime', 'pedro', 'eva', 'virginia', 'alberto', 'carla']
new_users = ['carlos', 'jon', 'EVA', 'lidia', 'Jaime', 'unai']


if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Lo sentimos, el nombre {new_user.title()} ya existe. Pruebe con un nombre diferente.")
        else:
            print(f"¡Enhorabuena, el usuario {new_user.title()} ha sido creado.")
else:
    print("Lo sentimos, no ha introducido ningún usuario.")