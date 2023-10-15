mundo_fantasia = {
    'argium' : {
        'vida': 850,
        'ataque': 258,
        'defensa': 12,
        'velocidad': 300,
        'sprint': 400,
        'ultimate': 'esfuerzo final',
        },
    'musegum' : {
        'vida': 1100,
        'ataque': 180,
        'defensa': 50,
        'velocidad': 280,
        'sprint': 350,
        'ultimate': 'quiebro',
        },
    'karmium' : {
        'vida': 3000,
        'ataque': 300,
        'defensa': 100,
        'velocidad': 30,
        'sprint': 60,
        'ultimate': 'mordedura de presa',
        },
    'dal lee' : {
        'vida': 900,
        'ataque': 260,
        'defensa': 15,
        'velocidad': 350,
        'sprint': 350,
        'ultimate': 'macho alfa',
        },
}

print("\t\tEsta es la lista de personajes del juego:")
for personaje in mundo_fantasia.keys():
    print("\t- " + personaje.title())

print("\n\t\tCaracterísticas de cada personaje:")
for personaje, caracteristicas in mundo_fantasia.items():
    print(f"\t- Personaje {personaje.title()}:")
    print(f"Puntos de vida: {caracteristicas['vida']}")
    print(f"Puntos de ataque: {caracteristicas['ataque']}")
    print(f"Puntos de defensa: {caracteristicas['defensa']}")
    print(f"Velocidad máxima: {caracteristicas['velocidad']}")
    print(f"Velocidad a sprint: {caracteristicas['sprint']}")
    print(f"Habilidad definitiva: {caracteristicas['ultimate']}")