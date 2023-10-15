import matplotlib.pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Crea un D6 y un D10.
die_1 = Die()
die_2 = Die()

#Hace algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(5_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analiza los resultados:
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


print(frequencies)
x_values = list(range(2, max_result+1))
print(x_values)

while True:
    
    #Traza los puntos del camino
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(20,12))
    x_values = list(range(2, max_result+1))
    ax.plot(x_values, frequencies)

    #Elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #plt.savefig('camino_aleatorio.png')
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break

