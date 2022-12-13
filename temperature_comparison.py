#Comparison of Local and Remote Temperature data on mean, standad deviation, minimum, maximum, and median.
#5 Rows, 2 Columns
#Column 0-1: Row 0-2: Local Temperature data, Row 3-5: Remote Temperature data
#Column 1-2: Row 0-1: Mean, Row 1-2: Standard Deviation, Row 2-3: Minimum, Row 3-4: Maximum, Row 4-5: Median

import requests
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from Functions import smoothing

plt.style.use('seaborn-v0_8-whitegrid')

#Local Data
data = {'hum': [31.1, 31.1, 33.3, 33.3, 40.1, 40.1, 40.1, 40.1, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 42.8, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 42.8, 42.8, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.1, 40.0, 40.0, 40.0, 40.0, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 37.9, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.1, 36.0, 36.0, 36.0, 36.0, 36.0, 36.0, 34.5, 34.5, 36.0, 36.0, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 36.0, 36.0, 36.0, 36.0, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 34.5, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 34.5, 34.5, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 33.1, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 33.1, 33.1, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.9, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 31.8, 31.8, 31.8, 31.8, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 30.7, 30.7, 30.7, 30.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 30.7, 30.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7, 29.7],
        'temp': [19.2, 19.2, 19.3, 19.3, 19.3, 19.3, 19.3, 19.3, 19.4, 19.4, 19.4, 19.4, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.5, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.6, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.7, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.8, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 19.9, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.1, 20.1, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2, 20.2]
        }

#Remote Data
readings = requests.get('http://192.168.6.142/readings').json()['readings'][0]
hum=[]
for sample in readings:
    if sample['sensor_id']==4 and 15025 < sample ['id'] < 36317:
        hum.append(sample['value'])
temp=[]
for sample in readings:
    if sample['sensor_id']==5 and 15024 < sample['id'] < 36316:
        temp.append(sample['value'])


#Dataset for the Temperature levels for Local location(5*12=60 minutes = hourly)
local_temp_mean_ph = []
local_temp_standard_dev_ph = []
local_temp_max_v_ph = []
local_temp_min_v_ph = []
local_temp_median_ph = []
for i in range(len(data['temp'])):
    local_temp_mean_ph.append(np.mean(data['temp'][i:i+12]))
    local_temp_standard_dev_ph.append(np.std(data['temp'][i:i+12]))
    local_temp_max_v_ph.append(max(data['temp'][i:i+12]))
    local_temp_min_v_ph.append(min(data['temp'][i:i+12]))
    local_temp_median_ph.append(np.median(data['temp'][i:i+12]))
#Dataset for the Temperature levels for Remote location(5*12=60 minutes = hourly)\
remote_temp_mean_ph = []
remote_temp_standard_dev_ph = []
remote_temp_max_v_ph = []
remote_temp_min_v_ph = []
remote_temp_median_ph = []
for i in range(len(temp)):
    remote_temp_mean_ph.append(np.mean(temp[i:i+12]))
    remote_temp_standard_dev_ph.append(np.std(temp[i:i+12]))
    remote_temp_max_v_ph.append(max(temp[i:i+12]))
    remote_temp_min_v_ph.append(min(temp[i:i+12]))
    remote_temp_median_ph.append(np.median(temp[i:i+12]))



#x_values for the Temperature levels for Local location
local_x_values = []
for i in range(len(data['temp'])):
    local_x_values.append(i)
#x_values for the Temperature levels for Remote location
remote_x_values = []
for i in range(len(temp)):
    remote_x_values.append(i)

fig1 = plt.figure(figsize=(10, 10))
gs = GridSpec(5,2)

#Local and Remote Temperature levels
for data,row1,row2,title,x_values in zip([data['temp'],temp],
                                         [0,3],
                                         [2,5],
                                         ['Temperature levels for Local location','Temperature levels for Remote location'],
                                         [local_x_values,remote_x_values]):
    x,y = smoothing(data)
    ax1 = fig1.add_subplot(gs[row1:row2,0:1])
    ax1.set_title(title,fontweight='bold')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature')
    ax1.plot(x, y, 'r')
    ax1.set_ylim(0,40)
    plt.plot(x,y, 'red', label='Smoothed')
    plt.title(title,fontweight='bold')
    #linear model(Local)
    m,b=np.polyfit(x_values,data,1)
    x_line = np.linspace(0, len(data), len(data))
    y_line = []
    for i in x_line:
        y_line.append(m*(i)+b)
    plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
    plt.legend()

#Comparisons of the Temperature levels for Local and Remote locations
for row1, row2, title, local_data, remote_data,y_lim in zip([0,1,2,3,4],
                                                            [1,2,3,4,5],
                                                            ['Mean Comparison', 'Standard Deviation Comparison', 'Max Value Comparison', 'Min Value Comparison', 'Median Comparison'],
                                                            [local_temp_mean_ph, local_temp_standard_dev_ph, local_temp_max_v_ph, local_temp_min_v_ph, local_temp_median_ph],
                                                            [remote_temp_mean_ph, remote_temp_standard_dev_ph, remote_temp_max_v_ph, remote_temp_min_v_ph, remote_temp_median_ph],
                                                            [[0, 40], [0, 2], [0, 40], [0, 40], [0, 40]]):
    #smoothing the local_data
    x,y = smoothing(local_data)
    #smoothing the remote_data
    x1,y1 = smoothing(remote_data)
    ax1 = fig1.add_subplot(gs[row1:row2, 1:2])
    ax1.set_title(title,fontweight='bold')
    ax1.set_ylabel('Temperature')
    ax1.plot(x, y, 'r')
    ax1.plot(x1, y1, 'b')
    ax1.set_ylim(y_lim)
    plt.plot(x, y, 'red', label='Local')
    plt.plot(x1, y1, 'blue', label='Remote')
    plt.title(title,fontweight='bold')
    plt.legend()
    if row2 == 5:
        ax1.set_xlabel('Time')
    plt.tick_params('x', labelbottom=False)
plt.tick_params('x', labelbottom=True)



#General Title
fig1.suptitle('Temperature level comparison for Local and Remote locations', fontsize=16, fontweight='bold', y=0.95, x=0.5, horizontalalignment='center')
#subtitle below general title
fig1.text(0.5, 0.92, '(All plots are smoothed.)', fontsize=12, horizontalalignment='center', verticalalignment='top')
plt.show()
