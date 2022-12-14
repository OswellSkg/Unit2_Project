![1a5uk0](https://user-images.githubusercontent.com/112055140/207366354-d44adfe8-d1ed-47e6-9987-4df76f3f5e14.jpg)


# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
The campus of UWC ISAK Japan is located in a small town on a mountain, Karuizawa. The altitude is 1251m, and the humidity as well as temperature is 
lower compared to that of the sea surface ground. From SKINKRAFT LABORATORY, the low humidity and temperature causes a lot of problems such as excessive sweating, acne breakout, anhidrosis and heat rash . For that reason, Student A from UWC ISAK Japan has requested an application to be updated of local temperature and humidity, and furthermore be updated of future temperature and humidity predictions for low-cost budget. This is also going to be used to help the client decide how they dress the next day accordingly to the predicted temperature and humidity.

Source: https://skinkraft.com/blogs/articles/how-does-humidity-affect-your-skin#how-does-humidity-affect-your-skin
https://www.mountain-forecast.com/peaks/Asama-Yama/forecasts/2568
https://fr.wikipedia.org/wiki/Mont_Asama

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. Other alternatives include diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python is open source, it is mature and supported in mutiple platforms (platform-independent) including macOS, Windows, Linux and can also be used to program the Arduino microprocessor [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  

**Design statement**

[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
## Success Criteria

1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours. 
1. ```[HL]``` The local variables will be measure using a set of 4 sensors around the dormitory.
2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. ```(SL: linear model)```, ```(HL: non-lineal model)```
3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
4. ```(SL)```The Local samples are stored in a csv file and ```(HL)``` posted to the remote server.
5. Create a prediction the subsequent 12 hours for both temperature and humidity.
6. A poster summarizing the visual representations, model and analysis is created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

# Criteria B: Design

## System Diagram **SL**

<img width="968" alt="Screen Shot 2022-12-13 at 9 44 03 PM" src="https://user-images.githubusercontent.com/112055140/207367039-e4b6b86d-2e1d-4aaf-a6df-03e6c2d44ea3.png">

**Fig.1** shows the system diagram for the proposed solution (**SL**). The indoor variables will be measured using an Arduino microprocessor and the sensor DHT11 conencted to the local computer (Laptop) located inside a room. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally.

## Record of Tasks

| Task No. | Planned Action                                     | Planned Outcome                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Time Estimate                                                               | Target Completion Date | Criterion |
|----------|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------|-----------|
| 1        | Write the <br>Problem definition                   | A clear definition of the problem is outlined, a thorough clarification of the client's needs can be observed, and the problem definition functions as a guide of work to complete the project.                                                                                                                                                                                                                                                                                           | 30 mins                                                                     | November 23rd          | A         |
| 2        | Write the <br>Design statement                     | Create the design statement in order to communicate with the client, the vision that Lison and I have as a solution to solve the client's problem and issues. Clarify the purpose fo the project as well, in regards to the needs of the client.                                                                                                                                                                                                                                          | 30 minutes                                                                  | November 25th          | A         |
| 3        | Create bill of work and<br> sign the Scope of Work | Create bill of work, sign the scope of work, and receive the necessary materials for the project.                                                                                                                                                                                                                                                                                                                                                                                         | 15 minutes                                                                  | November 25th          | A         |
| 4        | Program and generate<br>new csv file               | Code a program that connects to Arduino through a USB cable, receives the data that the Arduino is sending to the connected laptop where the program is operating, and append the data into a CSV file created specifically for this project named, "hum_temp_database.csv."                                                                                                                                                                                                              | 2 hours                                                                     | November 26th-27th     | C         |
| 4.5      | Create MVP<br>(Minimum Viable Product)             | Finalize the framework of the program for Arduino that will receive and process the datas sent by the DHT11 sensor.                                                                                                                                                                                                                                                                                                                                                                       | 1 hour                                                                      | November 30th          | C         |
| 5        | Collect Data                                       | Use DHT11, Arduino, and USB cable on Lison's laptop and establish a connection between DHT11 and Lison's laptop. Start data collection with the program written with Python and store the data in the CSV file for future immediate use.                                                                                                                                                                                                                                                  | 48 hours                                                                    | December 7th to 9th    | C         |
| 6        | Create visual <br>Representation                   | Create a visual representation from the collected data using the NumPy library and the matplotlib library. Graph plots from the data, separated into two groups, local and remote. Each group is then divided into two pictures, one dedicated to humidity, and the other dedicated to temperature. Each picture has a raw and smoothed version of the graph. Each graph has the mean, standard deviation, maximum, minimum, and median of the respective data. A total of 8 graphs made. | 8 hours<br>(+4 more hours<br>for revision<br>and improvement<br>on Dec 9th) | December 10th          | C         |
| 7        | Create linear model                                | From the graphs made from the step above, also create a linear model that would fit each of the graphs made. The linear model will function to suggest the general changes of humidity or temperature over time on each of the graphs. A total of 8 linear models made.                                                                                                                                                                                                                   | 5 hours                                                                     | December 6th           | C         |
| 8        | Create <br>Comparative Analysis                    | From the 8 graphs made for the mean, standard deviation, maximum, minimum, and median of the respective data, creating comparative data analysis graphs for Humidity and Temperature levels for each local and remote location.                                                                                                                                                                                                                                                           | 12 hours                                                                    | December 10th          | C         |
| 9        | Write the test plan                                | Complete the test plan for the programs written for this project. Clearly address the input, process, and intended output of the software testings.                                                                                                                                                                                                                                                                                                                                       | 1 hour                                                                      | December 10th          | B         |
| 10       | Create System Diagram                              | Create a system diagram for the client to show an overview of the scope of work and what kind of technology is being used for the project.(Arduino, DHT11 sensor, USB cable, etc.)                                                                                                                                                                                                                                                                                                        | 1 hour                                                                      | December 10th          | B         |
| 11       | Write and describe<br>flowcharts                   | Write flowcharts of specific parts of the program to provide an insight to the client of what the program looks like. Add descriptions so it is easy to understand. Clarify how the data is stored as well.                                                                                                                                                                                                                                                                               | 1 hour                                                                      | December 10th          | B         |
| 12       | Criterion C: Development                           | Add "Existing Tools," "Sources," and "Show your CTs" in the repository.                                                                                                                                                                                                                                                                                                                                                                                                                   | 1 hour                                                                      | December 10th          | C         |
| 13       | Insert the graphs created<br>into the repository.  | Insert the graphs created into the repository in the means of keeping record.                                                                                                                                                                                                                                                                                                                                                                                                             | 30 minutes                                                                  | December 10th          | B         |
| 14       | Create science poster                              | Create a poster, the ultimate product of the problem definition AND the graphs created. The poster will address both of them, and ultimately conclude a feasible conclusion to the problem that the client has introduced initially.                                                                                                                                                                                                                                                      | 1 hour                                                                      | December 13th          | D         |
| 15       | Take video                                         | Take a video explaining and guiding the audiences, clients over the success criteria and how different parts of our program fulfills each of the criterias.                                                                                                                                                                                                                                                                                                                               | 15 minutes                                                                  | December 13th          | D         |
| 16       | Finalize the repository                            | Finalize all the changes made to the repository, finalize program, finalize repository, ready everything for submission.                                                                                                                                                                                                                                                                                                                                                                  | 1 hour                                                                      | December 13th          | B         |
| 17       | Submit.                                            | Client is happy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 1 second                                                                    | December 13th          | B         |

## Test Plan

| **Software Testing:**                  | **Input:**                                                                                                                                        | **Process:**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Planned Outcome:**                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Functional: <br>Unit Testing           | Program to receive humidity and temperature data <br>from DHT11 sensor through the Arduino.                                                       | 1. Set up DHT11 sensor on Arduino<br>2. Connect laptop to Arduino<br>3. Run the coded program<br>4. Make visual confirmation that<br>the humidity and temperature is<br>being recorded from the DHT11 sensor<br>and put into a csv database file.                                                                                                                                                                                                                                                                                                              | The program is properly<br>processing the data gathered<br>from the DHT11 sensor into<br>a csv database file. The processing<br>is seamlessly and effectively done<br>so that it does not require additional<br>processing of the data afterwards, <br>and the data is ready for immediate use.                                                                                           |
| Functional: <br>Integration Testing    | The DHT11 sensor is acquiring accurate humidity<br>and temperature data, and sending proper data<br>to the laptop through the Arduino.            | 1. Set up the DHT11 sensor on Arduino<br>2. Connect the laptop to Arduino<br>3.1. Run the coded program in a warm room<br>and record the temperature and humidity.<br>3.2. Run the coded program outside in <br>cold weather and record the temperature<br>and humidity. <br>4. Verify that the data are accurate<br>and change accordingly to the location. <br>Ex. Warm place, cold place, humid place, etc.                                                                                                                                                 | The two different datas collected shows<br>proof that the DHT11 sensor is collecting<br>accurate humidity and temperature data. <br>Furthermore, the collection of data is <br>consistent and remains accurate. The data<br>is properly sent to the laptop without any<br>bugs. DHT11 sensor is fully functional and<br>supports the collection of data on the laptop<br>through Arduino. |
| Functional: <br>Unit Testing           | The program that graphs the humidity and temperature<br>data received from the DHT11 sensor through the<br>Arduino.                               | 1. Process humidity and temperature datas <br>into a csv database file. <br>2. Use the database file to list the mean,<br>standard deviation, maximum and minimum of<br>the collected data.<br>3. Process those values into a graph with the<br>program.                                                                                                                                                                                                                                                                                                       | The program produces and clear and an <br>easy-to-undersatnd graph from the given datas.<br>The program processes the datas correctly, and<br>does not have any malfunctions that could sabotage<br>the process.                                                                                                                                                                          |
| Non-Functional:<br>Usability Testing   | The program that receives humidity and temperature<br>data from the DHT11 sensor through the Arduino <br>writes its data in an user-friendly way. | 1. Have the DHT11 sensor and Arduino set up and<br>connected to the laptop.<br>2. Execute the program on PyCharm. <br>3. Make sure that every writes that the program <br>makes is accompanied with the date and time of <br>when the action is taken. <br>4. Confirm consistency and sustainability of <br>this program.                                                                                                                                                                                                                                      | The program produces clear and user-friendly<br>csv database file that can be immediately<br>put into use. This is achieved by an organized and<br>easy-to-understand interface produced by the program.<br>Each writes that the program makes will have date <br>and time to make it easier for the user to process<br>data afterwards.                                                  |
| Non-Functional:<br>Performance Testing | The program that receives humidity and <br>temperature data from the DHT11 sensor through <br>the Arduino executes its action every 5 minutes.    | 1. Have the DHT11 sensor and Arduino set up<br>and connected to the laptop. <br>2. Execute the program on PyCharm. <br>3. Confirm that the imported data from the DHT11<br>sensor through Arduino is written on the csv<br>database file every 5 minutes.                                                                                                                                                                                                                                                                                                      | The program demonstrates excellent performance<br>that executes every 5 minutes. The program writes<br>the collected data in the csv database file every<br>5 minutes, and produces an organized database file<br>that can be immediately put into use.                                                                                                                                   |
| Non-Functional:<br>Usability Testing   | The program that graphs the humidity and temperature<br>data received from the DHT11 sensor through the<br>Arduino.                               | 1. Process humidity and temperature datas <br>into a csv database file.<br>2. Use the database file to list the mean, <br>sstandard deviation, maximum and minimum of the<br>collected data.<br>3. Process those values into a graph with the<br>program. <br>4. Verify that the graph is easy-to-understand<br>and uses color variations to clarify different<br>values on the graph. <br>5. Each values are clearly labelled and other <br>unclear factors that could negatively impact <br>the graph is clarified through the use of <br>labels and colors. | The program produces easy-to-understand graphs that<br>is user-friendly for immediate use. The graphs produced<br>use labels and colors to make it easy for users to<br>not only understand but also put into use in a lot of ways.<br>There are no bugs found in the program, and the graphs<br>maintain a solid quality regardless of the quality of<br>the collected data.             |

## Flow diagrams
<br>

![flow chart 2 drawio](https://user-images.githubusercontent.com/112055140/207601967-fbba7250-1a69-4804-b8e1-1cfffbae2420.png)

**fig1**: 
<br><br><br>

![flow chart 3 drawio](https://user-images.githubusercontent.com/112055140/207601997-188beeec-ed61-4a81-8249-d10060525da3.png)

**fig2**:
<br><br><br>

![flow diagram 1 (1)](https://user-images.githubusercontent.com/112055140/207601988-d16cbf68-1ad7-4c5c-9a31-6a72558252de.jpg)

**fig3**:
<br><br>

## Data storage method

```.py
import serial
import time
from datetime import datetime
import schedule

arduino = serial.Serial(port='/dev/cu.usbserial-1420', baudrate=9600, timeout=.1)

def read():
    data = ""
    while len(data)<1:
        data = arduino.readline()
    return data
```
**fig.1**: Code from "arduino.py"(https://github.com/OswellSkg/Unit2_Project/blob/main/arduino.py)

The code above in figure 1 is importing a number of libraries necessary to connect to the Arduino, and is connecting to the Arduino and is receiving the data from Arduino per line. 
<br><br>


```.py
data = {
    "hum": [],
    "temp": [],
}

def append_data():
    value = read() #wait until data is in the port
    msg = value.decode('utf-8')
    if not 'Hello' in msg:
        msg = msg.split()
        hum = msg[0].split(':')[1]
        temp = msg[1].split(':')[1]
        hum = float(hum[0:5])
        temp = float(temp[0:5])
        data["hum"].append(hum)
        data["temp"].append(temp)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        with open("hum_temp_database.csv", "a") as file:
            file.write(f'\n{dt_string},{hum},{temp}')

dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Starting data collection at {dt_string}")

schedule.every(5).minutes.do(append_data)
while True:
    schedule.run_pending()
    time.sleep(1)
```
**fig2**: Code from "arduino.py"[https://github.com/OswellSkg/Unit2_Project/blob/main/arduino.py]

The code above in the figure 2 is creating a dictionary for two lists, "hum" and "temp." After that, it is appending the data received from the Arduino into a csv file named "hum_temp_database.csv" along with the live date and time. It is also appending the humidity and temperature values into the lists in the dictionary. This process is executed every 5 minutes. 
<br><br>


<img width="320" alt="Screen Shot 2022-12-13 at 21 21 23" src="https://user-images.githubusercontent.com/112055140/207316682-2fa8d834-db2e-474d-b17a-2804d4490eb3.png">

**fig3**: A screenshot of the csv file, "hum_temp_database.csv"(https://github.com/OswellSkg/Unit2_Project/blob/main/hum_temp_database.csv)

The screenshot above in figure 3 shows how the data received from Arduino is being appeneded into "hum_temp_database.csv" with live date and time. As seen in the screenshot, the append happens per line. First comes the date, followed with the time, and finally humidity and temperature. This is happening every 5 minutes for 48 hours, resulting in a total of 577 lines. 
<br><br>


<img width="374" alt="Screen Shot 2022-12-13 at 21 26 51" src="https://user-images.githubusercontent.com/112055140/207317790-58498456-7c12-405d-942e-4d5a8f5f6eb1.png">

**fig4**: A screenshot of the dictionary that includes the 'hum' and 'temp' lists(https://github.com/OswellSkg/Unit2_Project/blob/main/hum_temp_database_dict.py)

The screenshot above in figure 4 shows the dictionary that includes the 'hum' and 'temp' lists. The dictionary makes it extremely easy for Lison and myself to process the data and plot it into a graph. 


# Criteria C: Development

## Existing Tools:
1. If statement
2. For loop
3. Functions
4. Variables
5. Dictionaries
6. Lists
7. File reading
8. File appending
9. Plotting graph
10. Request/Get from server


## Libraries used:
1. Matplotlib
2. Requests
3. Numpy
4. Serial
5. Time
6. Datetime
7. Schedule


## Success Criterias:


### 1. The solution provides a visual representation of the Humidity and Temperature values inside a dormitory (Local) and outside the house (Remote) for a period of minimum 48 hours.
<br>

We used Matplotlib library to plot the Humidity and Temperature of both Local and Remote locations over a period of 48 hours, and visually represent the datas colelcted. Over the process, we also read from the 'hum' and 'temp' lists in the data dictionary that we stored the Humidity and Temperature data of Local location, and also used requests library in order to obtain Humidity and Temperature datas of Remote location. 

```.py
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
```
<img width="715" alt="Screen Shot 2022-12-13 at 22 09 30" src="https://user-images.githubusercontent.com/112055140/207326976-a21e200e-2cc3-4d3b-a31f-16b3964de049.png">

**fig1**: Visual Representation of Humidity for Local(Code&Graph)
<br><br><br>

```.py
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
```
<img width="743" alt="Screen Shot 2022-12-13 at 22 10 12" src="https://user-images.githubusercontent.com/112055140/207327037-e8891d9e-12fe-4bdc-bb9a-8eecc683d60e.png">

**fig2**: Visual Representation of Temperature for Local(Code&Graph)
<br><br><br>

```.py
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
```
<img width="719" alt="Screen Shot 2022-12-13 at 22 10 24" src="https://user-images.githubusercontent.com/112055140/207327058-92ae2eb8-cfc6-47cf-acad-7c54d07bee6e.png">

**fig3**: Visual Representation of Humidity for Remote(Code&Graph)
<br><br><br>

```.py
#Smoothed Plot of the Temperature levels for Remote location
x,y = smoothing(temp)
ax1 = fig2.add_subplot(gs[1:2,:])
ax1.set_title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
ax1.set_xlabel('Time')
ax1.set_ylabel('Humidity')
ax1.plot(x, y, 'r')
ax1.set_ylim([0, 35])
plt.plot(x,y, 'red', label='Smoothed')
plt.title('Smoothed Graph', fontsize=14, fontweight='bold', y=1, x=0.5, color='black', horizontalalignment='center')
```
<img width="723" alt="Screen Shot 2022-12-13 at 22 10 49" src="https://user-images.githubusercontent.com/112055140/207327081-5c99a231-be97-4dc3-9959-d82fbce5acdd.png">

**fig4**: Visual Representation of Temperature for Remote(Code&Graph)
<br><br>

### 2. The solution provides a mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. (SL: linear model), (HL: non-lineal model)
<br>
We used NumPy library and Matplotlib library to plot a linear model of best fit for each of the graphs. First, we used Numpy in order to idetify the slope of the linear equation, using variables m and b. Then we used the Matplotlib library to plot the linear equation across the graph. 

```.py
#linear model for Humidity levels for Local location
m,b=np.polyfit(x_values,data['hum'],1)
x_line = np.linspace(0, len(data['hum']), len(data['hum']))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
```
<img width="715" alt="Screen Shot 2022-12-13 at 22 09 30" src="https://user-images.githubusercontent.com/112055140/207326976-a21e200e-2cc3-4d3b-a31f-16b3964de049.png">

**fig1**: Linear model of Humidity for Local(Code&Graph)
<br><br><br>

```.py
#linear model for Temperature levels for Local location
m,b=np.polyfit(x_values,data['temp'],1)
x_line = np.linspace(0, len(data['temp']), len(data['temp']))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
```
<img width="743" alt="Screen Shot 2022-12-13 at 22 10 12" src="https://user-images.githubusercontent.com/112055140/207327037-e8891d9e-12fe-4bdc-bb9a-8eecc683d60e.png">

**fig2**: Linear model of Temperature for Local(Code&Graph)
<br><br><br>

```.py
#linear model for Humidity levels for Remote location
m,b=np.polyfit(x_values,hum,1)
x_line = np.linspace(0, len(hum), len(hum))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
```
<img width="719" alt="Screen Shot 2022-12-13 at 22 10 24" src="https://user-images.githubusercontent.com/112055140/207327058-92ae2eb8-cfc6-47cf-acad-7c54d07bee6e.png">

**fig3**: Linear model of Humidity for Remote(Code&Graph)
<br><br><br>

```.py
#linear model for Temperature levels for Remote location
m,b=np.polyfit(x_values,temp,1)
x_line = np.linspace(0, len(temp), len(temp))
y_line = []
for i in x_line:
    y_line.append(m*(i)+b)
plt.plot(x_line,y_line,'dodgerblue', label='Linear Model')
```
<img width="723" alt="Screen Shot 2022-12-13 at 22 10 49" src="https://user-images.githubusercontent.com/112055140/207327081-5c99a231-be97-4dc3-9959-d82fbce5acdd.png">

**fig4**: Linear model of Temperature for Remote(Code&Graph)
<br><br>

### 3. The solution provides a comparative analysis for the Humidity and Temperature levels for each Local and Remote locations including mean, standad deviation, minimum, maximum, and median.
<br>

```.py
#Comparisons of the Humidity levels for Local and Remote locations
for row1, row2, title, local_data, remote_data,y_lim in zip([0,1,2,3,4],
                                                            [1,2,3,4,5],
                                                            ['Mean Comparison', 'Standard Deviation Comparison', 'Max Value Comparison', 'Min Value Comparison', 'Median Comparison'],
                                                            [local_hum_mean_ph, local_hum_standard_dev_ph, local_hum_max_v_ph, local_hum_min_v_ph, local_hum_median_ph],
                                                            [remote_hum_mean_ph, remote_hum_standard_dev_ph, remote_hum_max_v_ph, remote_hum_min_v_ph, remote_hum_median_ph],
                                                            [[10, 50], [0, 2], [10, 50], [10, 50], [10, 50]]):
    #smoothing the local_data
    x,y = smoothing(local_data)
    #smoothing the remote_data
    x1,y1 = smoothing(remote_data)
    ax1 = fig1.add_subplot(gs[row1:row2, 1:2])
    ax1.set_title(title,fontweight='bold')
    ax1.set_ylabel('Humidity')
    ax1.plot(x, y, 'r')
    ax1.plot(x1, y1, 'b')
    ax1.set_ylim(y_lim)
    plt.plot(x, y, 'red', label='Local')
    plt.plot(x1, y1, 'blue', label='Remote')
    plt.title(title,fontweight='bold')
    plt.legend(loc="upper right")
    if row2 == 5:
        ax1.set_xlabel('Time')
    plt.tick_params('x', labelbottom=False)
plt.tick_params('x', labelbottom=True)
```
<img width="350" alt="Screen Shot 2022-12-13 at 23 47 01" src="https://user-images.githubusercontent.com/112055140/207365120-da44fa8b-342b-4066-a948-5388ff6a5db0.png">

**fig1**: Comparative Analysis for Humidity for Local and Remote Locations(Code&Graph)
<br><br><br>

```.py
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
```
<img width="360" alt="Screen Shot 2022-12-13 at 23 47 48" src="https://user-images.githubusercontent.com/112055140/207365291-897e3d93-39b3-43d4-ab2e-a32dfdd1ea35.png">

**fig2**: Comparative Analysis for Temperature for Local and Remote Locations
<br><br>

### 4. (SL)The Local samples are stored in a csv file and (HL) posted to the remote server.
<br>

```.py
def append_data():
    value = read() #wait until data is in the port
    msg = value.decode('utf-8')
    if not 'Hello' in msg:
        msg = msg.split()
        hum = msg[0].split(':')[1]
        temp = msg[1].split(':')[1]
        hum = float(hum[0:5])
        temp = float(temp[0:5])
        data["hum"].append(hum)
        data["temp"].append(temp)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(data)
        with open("hum_temp_database.csv", "a") as file:
            file.write(f'\n{dt_string},{hum},{temp}')
```

**fig1**: A function that appends data into the csv file, "hum_temp_database.csv"
<br><br><br>

<img width="651" alt="Screen Shot 2022-12-13 at 23 28 31" src="https://user-images.githubusercontent.com/112055140/207359989-b0ce6f30-1f53-4bff-854a-8149b8c9054d.png">

**fig2**: A screenshot of the csv file, "hum_temp_database.csv"
<br><br>

### 5. Create a prediction the subsequent 12 hours for both temperature and humidity.
<br>

```.py
#Prediction Line for Humidity for Local location
prediction_line = np.linspace(len(data['hum']), len(data['hum'])*5//4, len(data['hum'])*5//4)
prediction_y_line = []
for i in prediction_line:
    prediction_y_line.append(m*(i)+b)
plt.plot(prediction_line, prediction_y_line, 'b--', label='Prediction')
```
<img width="715" alt="Screen Shot 2022-12-13 at 22 09 30" src="https://user-images.githubusercontent.com/112055140/207326976-a21e200e-2cc3-4d3b-a31f-16b3964de049.png">

**fig1**: Prediction Line for Humidity for Local(Code&Graph)
<br><br><br>

```.py
#Prediction Line for Temperature for Local location
prediction_line = np.linspace(len(data['temp']), len(data['temp'])*5//4, len(data['temp'])*5//4)
prediction_y_line = []
for i in prediction_line:
    prediction_y_line.append(m*(i)+b)
plt.plot(prediction_line, prediction_y_line, 'b--', label='Prediction')
```
<img width="743" alt="Screen Shot 2022-12-13 at 22 10 12" src="https://user-images.githubusercontent.com/112055140/207327037-e8891d9e-12fe-4bdc-bb9a-8eecc683d60e.png">

**fig2**: Prediction Line for Temperature for Local(Code&Graph)
<br><br><br>

```.py
#Prediction Line for Humidity for Remote location
p = np.poly1d(np.polyfit(x_morning_to_noon,hum_morning_to_noon,1))
x_line = [len(hum),len(hum)+len(hum_morning_to_noon)]
plt.plot(x_line,p(x_line)+35,'b--',label='Linear Model(Prediction)')
```
<img width="719" alt="Screen Shot 2022-12-13 at 22 10 24" src="https://user-images.githubusercontent.com/112055140/207327058-92ae2eb8-cfc6-47cf-acad-7c54d07bee6e.png">

**fig3**: Prediction Line for Humidity for Remote(Code&Graph)
<br><br><br>

```.py
#Prediction Line for Temperature for Remote location
p = np.poly1d(np.polyfit(x_morning_to_noon,temp_morning_to_noon,1))
x_line = [len(temp),len(temp)+len(temp_morning_to_noon)]
plt.plot(x_line,p(x_line)-20,'b--',label='Linear Model(Prediction)')
```
<img width="723" alt="Screen Shot 2022-12-13 at 22 10 49" src="https://user-images.githubusercontent.com/112055140/207327081-5c99a231-be97-4dc3-9959-d82fbce5acdd.png">

**fig4**: Prediction Line for Temperature for Remote(Code&Graph)
<br><br>



### 6. A poster summarizing the visual representations, model and analysis is created. The poster includes a recommendation about healthy levels for Temperature and Humidity.

Paste code

Figx: this code shows blah blah

According to figx and explain code and techniques used. To come up with this idea we used decomposition which is a part of computational thinking and we break the problem down to 2 parts which are measuing inside and outside…

mathematical modelling for the Humidity and Temperature levels for each Local and Remote locations. (In bold)
Paste code and do the same as before for this

## Sources

## Show your CTs


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
