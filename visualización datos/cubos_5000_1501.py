#Cubos
import matplotlib.pyplot as plt



x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis, s=10)


#Establece el título del gráfico y las etiquetas de los ejes.
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)

#Establece el tamaño de las etiquetas de los puntos de los ejes.
ax.tick_params(axis='both', which='major', labelsize=14)

#Establece el rango para cada eje
ax.axis([0, 5000, 0, 125_000_000_000])


plt.savefig('cubed_plot_15.1b.png')
plt.show()