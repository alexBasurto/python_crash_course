import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/bilbao_airport_1947_2023_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Obtiene fechas y temperaturas máximas y mínimas de este archivo
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        try:
            high = float(row[8])
            low = float(row[9])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Traza las temperaturas máximas
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Da formato al trazado
title = "Daily high and low temperatures - 1947-2023\nBilbao Aeropuerto, SP"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (Cº)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()