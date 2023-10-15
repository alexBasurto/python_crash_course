libros = ['hamlet', 'le_comte_de_montecristo', 'the_adventures_of_roderick_random']

for libro in libros:
    try:
        with open(f"cap10\\libros\\{libro}.txt", "r", encoding="utf-8") as fo:
            contenido = fo.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nTítulo: {libro.upper()}")
        print(f"\t - Palabras como the, there, then...: {contenido.lower().count('the')} palabras.")
        print(f"\t - Palabras the: {contenido.lower().count('the ')} palabras.")