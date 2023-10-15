#Alex Basurto, 17-06-2023. Imprime el nombre dado 4 veces, metiendo un salto de linea y una tabulación, y eliminando los espacios de las distintas formas posibles.
nombre = "  Lidia Vivanco   "
print(f"\t {nombre}")
print(f"\n\t {nombre.lstrip()}")
print(f"\n\t{nombre.rstrip()}")
print(f"\n\t{nombre.strip()}")