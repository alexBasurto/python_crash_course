bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(bicycles[3].title())
#con menos uno accedemos al último elemento de la lista, lo vemos a continuación:
print(f"\n{bicycles[-1].title()}")
#menos 2 nos devuelve el anteúltimo, menos 3 nos devuelve el antepenúltimo...

message = f"Mi primera bici fue una {bicycles[0].title()}."
print(message)