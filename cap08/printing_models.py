# Empieza con unos diseños que hay que imprimir.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula la impresión de cada diseño hasta que no queda ninguno.
# Mueve cada diseño a completed_models después de la impresión.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Muestra todos los modelos completados.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)