#la cadena if-elif-else

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65: #else: / si podemos evitar else, mejor. Bajo else puede caber cualquier tipo de dato, es demasiado abierto. Usar solo if-elif-elif-... ofrece más garantías.
    price = 20

print(f"Your admission cost is ${price}.")