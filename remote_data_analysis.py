# The solution provides a comparative analysis for the
# Humidity and Temperature levels for each Local and Remote locations including
# mean, standard deviation, minimum, maximum, and median.

import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from Functions import smoothing

plt.style.use('seaborn-v0_8-whitegrid')

#Get data from the server
readings = requests.get('http://192.168.6.142/readings').json()['readings'][0]

#Get only Humidity levels from Remote location
hum=[]
for sample in readings:
    if sample['sensor_id']==4 and 15025 < sample ['id'] < 36317:
        hum.append(sample['value'])

#Get only Temperature levels from Remote location
temp=[]
for sample in readings:
    if sample['sensor_id']==5 and 15024 < sample['id'] < 36316:
        temp.append(sample['value'])

#Dataset for the Humidity levels for Remote location(5*12=60 minutes = hourly)\
hum_mean_ph = []
hum_standard_dev_ph = []
hum_max_v_ph = []
hum_min_v_ph = []
hum_median_ph = []
for i in range(len(hum)):
    hum_mean_ph.append(np.mean(hum[i:i+12]))
    hum_standard_dev_ph.append(np.std(hum[i:i+12]))
    hum_max_v_ph.append(max(hum[i:i+12]))
    hum_min_v_ph.append(min(hum[i:i+12]))
    hum_median_ph.append(np.median(hum[i:i+12]))

#Dataset for the Temperature levels for Remote location(5*12=60 minutes = hourly)
temp_mean_ph = []
temp_standard_dev_ph = []
temp_max_v_ph = []
temp_min_v_ph = []
temp_median_ph = []
for i in range(len(temp)):
    temp_mean_ph.append(np.mean(temp[i:i+12]))
    temp_standard_dev_ph.append(np.std(temp[i:i+12]))
    temp_max_v_ph.append(max(temp[i:i+12]))
    temp_min_v_ph.append(min(temp[i:i+12]))
    temp_median_ph.append(np.median(temp[i:i+12]))

#x_values for the Humidity levels for Remote location
x_values = []
for i in range(len(hum)):
    x_values.append(i)

#General setup for the plot
fig1 = plt.figure(figsize=(10, 10))
gs = GridSpec(2,2)

#Plot the Humidity levels for Remote location
plt.suptitle('Humidity levels for Remote location', fontsize=16, fontweight='bold', y=0.95, x=0.5, color='black', horizontalalignment='center')
ax1 = fig1.add_subplot(gs[0:1,:])
ax1.set_title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x_values, hum, 'r')
ax1.set_ylim([0, 60])
plt.plot(x_values,hum_mean_ph, 'red', label='Mean')
plt.plot(x_values,hum_standard_dev_ph, 'green', label='Standard Deviation')
plt.plot(x_values,hum_max_v_ph, 'blue', label='Maximum')
plt.plot(x_values,hum_min_v_ph, 'yellow', label='Minimum')
plt.plot(x_values,hum_median_ph, 'black', label='Median')
plt.legend()
plt.title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#Smoothed Plot of the Humidity levels for Remote location
x,y = smoothing(hum)
ax1 = fig1.add_subplot(gs[1:2,:])
ax1.set_title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x, y, 'r')
ax1.set_ylim([0, 60])
plt.plot(x,y, 'red', label='Smoothed')
plt.title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#linear model
m,b=np.polyfit(x_values,hum,1)
x_line = np.linspace(0, len(hum), len(hum))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
#slice temperature to the region of interest
hum_morning_to_noon = hum[0:len(x_values)//4]
x_morning_to_noon = range(len(hum_morning_to_noon))
#Plot the prediction
p = np.poly1d(np.polyfit(x_morning_to_noon,hum_morning_to_noon,1))
x_line = [len(hum),len(hum)+len(hum_morning_to_noon)]
plt.plot(x_line,p(x_line)+35,'b--',label='Linear Model(Prediction)')
plt.legend()
plt.show()

#General setup for the plot
fig2 = plt.figure(figsize=(10, 10))
gs = GridSpec(2, 2)

#Plot the Temperature levels for Remote location
plt.suptitle('Temperature levels for Remote location', fontsize=16, fontweight='bold', y=0.95, x=0.5, color='black', horizontalalignment='center')
ax1 = fig2.add_subplot(gs[0:1,:])
ax1.set_title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Temperature')
ax1.plot(x_values, temp, 'r')
ax1.set_ylim([0, 35])
plt.plot(x_values,temp_mean_ph, 'red', label='Mean')
plt.plot(x_values,temp_standard_dev_ph, 'green', label='Standard Deviation')
plt.plot(x_values,temp_max_v_ph, 'blue', label='Maximum')
plt.plot(x_values,temp_min_v_ph, 'yellow', label='Minimum')
plt.plot(x_values,temp_median_ph, 'black', label='Median')
plt.legend()
plt.title('Raw Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#Smoothed Plot of the Temperature levels for Remote location
x,y = smoothing(temp)
ax1 = fig2.add_subplot(gs[1:2,:])
ax1.set_title('Smoothed Graph')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x, y, 'r')
ax1.set_ylim([0, 35])
plt.plot(x,y, 'red', label='Smoothed')
plt.title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
#linear model
m,b=np.polyfit(x_values,temp,1)
x_line = np.linspace(0, len(temp), len(temp))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')

#slice temperature to the region of interest
temp_morning_to_noon = temp[0:len(x_values)//4]
x_morning_to_noon = range(len(temp_morning_to_noon))

#Plot the linear model(Prediction)
p = np.poly1d(np.polyfit(x_morning_to_noon,temp_morning_to_noon,1))
x_line = [len(temp),len(temp)+len(temp_morning_to_noon)]
plt.plot(x_line,p(x_line)-20,'b--',label='Linear Model(Prediction)')

plt.legend()
plt.show()
