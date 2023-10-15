from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Crea un D6 y un D10.
die_1 = Die()
die_2 = Die(10)

#Hace algunas tiradas y guarda los resultados en una lista.
results = [die_1.roll() + die_2.roll() for result in range(50_000)]

#Analiza los resultados:
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza los resultados.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
    xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10_comprension_listas.html')