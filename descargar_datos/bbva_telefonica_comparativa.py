import csv
from datetime import datetime

import matplotlib.pyplot as plt

def processCSV(filename, symbol="encoding='UTF-8'"):
    """
    Indicamos directorio del fichero con precio de acción y su codificación.
    Codificación por defecto: UTF-8
    """

    with open(filename, encoding='UTF-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        ixFecha = header_row.index('\ufeff"Fecha"')
        ixUltimo = header_row.index('Último')
        ixApertura = header_row.index('Apertura')
        ixMax = header_row.index('Máximo')
        ixMin = header_row.index('Mínimo')

        # Obtiene fechas y temperaturas máximas y mínimas de los archivos
        fechas, ultimos, aperturas, maximos, minimos = [], [], [], [], []
        for row in reader:
            current_date = datetime.strptime(row[ixFecha], "%d.%m.%Y")
            try:
                ultimo = float(row[ixUltimo].replace(',','.'))
                apertura = float(row[ixApertura].replace(',','.'))
                maximo = float(row[ixMax].replace(',','.'))
                minimo = float(row[ixMin].replace(',','.'))
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                fechas.append(current_date)
                ultimos.append(ultimo)
                aperturas.append(apertura)
                maximos.append(maximo)
                minimos.append(minimo)

    return fechas, ultimos, aperturas, maximos, minimos

data_files = [
    ('data/bbva_2021_2023.csv', 'BBVA', 'red'),
    ('data/telefonica_2021_2023.csv', 'Telefónica', 'blue'),
    ('data/repsol_2021_2023.csv', 'Repsol', 'green'),
    ('data/iberdrola_2021_2023.csv', 'Iberdrola', 'yellow')
]

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(18, 9.5))

for filename, company, color in data_files:
    fechas, ultimos, aperturas, maximos, minimos = processCSV(filename)
    # Traza valores
    ax.plot(fechas, ultimos, c=color, alpha=0.5, linewidth=2, label=f"Precio {company}")
    ax.plot(fechas, minimos, c=color, alpha=0.5, linewidth=0.5, label=f"Mínimo {company}")
    ax.plot(fechas, maximos, c=color, alpha=0.5, linewidth=0.5, label=f"Máximo {company}")
    plt.fill_between(fechas, maximos, minimos, facecolor='red', alpha=0.1)
    
ax.legend()


# Da formato al trazado
title = f"Comparativa datos históricos 2021 - 2023\n"
company_names = [company for _, company, _ in data_files]
title += " - ".join(company_names)

plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precio acción", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()