#Forma tradicional
cubos = []
for value in range(1, 11):
    cubos.append(value**3)
print(cubos)

#Lista por comprensión (ejer. 4.9)
cubos = [value**3 for value in range(1, 11)]
print(cubos)