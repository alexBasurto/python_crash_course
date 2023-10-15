import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename1 = 'data/new_york_upton_coop_2023_simple.csv'
filename2 = 'data/boston_2023_simple.csv'

with open(filename1) as f1, open(filename2) as f2:
    reader1 = csv.reader(f1)
    reader2 = csv.reader(f2)
    loc1 = list(reader1)[1][1]
    loc2 = list(reader2)[1][1]
    # Reiniciamos la iteración de los archivos
    f1.seek(0)
    f2.seek(0)
    header_row1 = next(reader1) # Líneas importantes para que CSV.READER salte a la línea 2
    header_row2 = next(reader2)
    ixDate1 = header_row1.index('DATE')
    ixDate2 = header_row2.index('DATE')
    ixMax1 = header_row1.index('TMAX')
    ixMax2 = header_row2.index('TMAX')
    ixMin1 = header_row1.index('TMIN')
    ixMin2 = header_row2.index('TMIN')

    # Obtiene fechas y temperaturas máximas y mínimas de los archivos
    dates1, dates2, highs1, highs2, lows1, lows2 = [], [], [], [], [], []
    for row in reader1:
        current_date1 = datetime.strptime(row[ixDate1], "%Y-%m-%d")
        try:
            high1 = int(row[ixMax1])
            low1 = int(row[ixMin1])
        except ValueError:
            print(f"Missing data for {current_date1}")
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)
    
    for row in reader2:
        current_date2 = datetime.strptime(row[ixDate2], "%Y-%m-%d")
        try:
            high2 = int(row[ixMax2])
            low2 = int(row[ixMin2])
        except ValueError:
            print(f"Missing data for {current_date2}")
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)
    


# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(18, 9.5))
ax.plot(dates1, highs1, c='red', alpha=0.5)
ax.plot(dates1, lows1, c='blue', alpha=0.5)
ax.plot(dates2, highs2, c='red', alpha=0.5)
ax.plot(dates2, lows2, c='blue', alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor='lightblue', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='lightgreen', alpha=0.1)

# Da formato al trazado
title = f"Daily high and low temperatures - 2018\n{loc1} + {loc2}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()