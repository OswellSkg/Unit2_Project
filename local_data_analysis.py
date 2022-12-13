# The solution provides a comparative analysis for the
# Humidity and Temperature levels for each Local and Remote locations including
# mean, standard deviation, minimum, maximum, and median.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from Functions import smoothing

plt.style.use('seaborn-v0_8-whitegrid')

data = {'hum': [31.1, 31.1, 33.3, 33.3, 40.1, 40.1, 40.1, 40.1, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 42.8, 42.8, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.0, 40.0, 40.0, 40.0, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.0, 36.0, 36.0, 36.0, 36.0, 36.0, 34.5, 34.5, 36.0, 36.0, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 36.0, 36.0, 36.0, 36.0, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 34.5, 34.5, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7],
        'temp': [19.2, 19.2, 19.3, 19.3, 19.3, 19.3, 19.3, 19.3, 19.4, 19.4, 19.4, 19.4, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2]
        }

#smoothing function
#smoothing()

#Dataset for the Humidity levels for Local location(5*12=60 minutes = hourly)
hum_mean_ph = []
hum_standard_dev_ph = []
hum_max_v_ph = []
hum_min_v_ph = []
hum_median_ph = []
for i in range(len(data['hum'])):
    hum_mean_ph.append(np.mean(data['hum'][i:i+12]))
    hum_standard_dev_ph.append(np.std(data['hum'][i:i+12]))
    hum_max_v_ph.append(max(data['hum'][i:i+12]))
    hum_min_v_ph.append(min(data['hum'][i:i+12]))
    hum_median_ph.append(np.median(data['hum'][i:i+12]))

#Dataset for the Temperature levels for Local location(5*12=60 minutes = hourly)
temp_mean_ph = []
temp_standard_dev_ph = []
temp_max_v_ph = []
temp_min_v_ph = []
temp_median_ph = []
for i in range(len(data['temp'])):
    temp_mean_ph.append(np.mean(data['temp'][i:i+12]))
    temp_standard_dev_ph.append(np.std(data['temp'][i:i+12]))
    temp_max_v_ph.append(max(data['temp'][i:i+12]))
    temp_min_v_ph.append(min(data['temp'][i:i+12]))
    temp_median_ph.append(np.median(data['temp'][i:i+12]))

#x_values for the Humidity levels for Local location
x_values = []
for i in range(len(data['hum'])):
    x_values.append(i)


#General setup for the plot
fig1 = plt.figure(figsize=(10, 10))
gs = GridSpec(2,2)

#Plot the Humidity levels for Local location
plt.suptitle('Humidity levels for Local location', fontsize=16, fontweight='bold', y=0.95, x=0.5, color='black', horizontalalignment='center')
ax1 = fig1.add_subplot(gs[0:1,:])
ax1.set_title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x_values, data['hum'], 'r')
ax1.set_ylim([20,45])
plt.plot(x_values,hum_mean_ph, 'red', label='Mean')
plt.plot(x_values,hum_standard_dev_ph, 'green', label='Standard Deviation')
plt.plot(x_values,hum_max_v_ph, 'blue', label='Maximum')
plt.plot(x_values,hum_min_v_ph, 'yellow', label='Minimum')
plt.plot(x_values,hum_median_ph, 'black', label='Median')
plt.legend()
plt.title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#Smoothed Plot of the Humidity levels for Local location
x,y = smoothing(data['hum'])
ax1 = fig1.add_subplot(gs[1:2,:])
ax1.set_title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x, y, 'r')
ax1.set_ylim([20, 45])
plt.plot(x,y, 'red', label='Smoothed')
plt.title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#linear model
m,b=np.polyfit(x_values,data['hum'],1)
x_line = np.linspace(0, len(data['hum']), len(data['hum']))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
#prediction line
prediction_line = np.linspace(len(data['hum']), len(data['hum'])*5//4, len(data['hum'])*5//4)
prediction_y_line = []
for i in prediction_line:
    prediction_y_line.append(m*(i)+b)
plt.plot(prediction_line, prediction_y_line, 'b--', label='Prediction')

plt.legend()
plt.show()


#General setup for the plot
fig2 = plt.figure(figsize=(10, 10))
gs = GridSpec(2, 2)

#Plot the Temperature levels for Local location
plt.suptitle('Temperature levels for Local location', fontsize=16, fontweight='bold', y=0.95, x=0.5, color='black', horizontalalignment='center')
ax1 = fig2.add_subplot(gs[0:1,:])
ax1.set_title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
ax1.plot(x_values, data['temp'], 'r')
ax1.set_ylim([19, 21])
plt.plot(x_values,temp_mean_ph, 'red', label='Mean')
plt.plot(x_values,temp_standard_dev_ph, 'green', label='Standard Deviation')
plt.plot(x_values,temp_max_v_ph, 'blue', label='Maximum')
plt.plot(x_values,temp_min_v_ph, 'yellow', label='Minimum')
plt.plot(x_values,temp_median_ph, 'black', label='Median')
plt.legend()
plt.title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#Smoothed Plot of the Temperature levels for Local location
x,y = smoothing(data['temp'])
ax1 = fig2.add_subplot(gs[1:2,:])
ax1.set_title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x, y, 'r')
ax1.set_ylim([19, 21])
plt.plot(x,y, 'red', label='Smoothed')
plt.title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#linear model
m,b=np.polyfit(x_values,data['temp'],1)
x_line = np.linspace(0, len(data['temp']), len(data['temp']))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
#prediction line
prediction_line = np.linspace(len(data['temp']), len(data['temp'])*5//4, len(data['temp'])*5//4)
prediction_y_line = []
for i in prediction_line:
    prediction_y_line.append(m*(i)+b)
plt.plot(prediction_line, prediction_y_line, 'b--', label='Prediction')
plt.legend()
plt.show()
