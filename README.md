![weather_asbt](https://user-images.githubusercontent.com/112055140/203181929-2ae57953-7af7-4940-9e1b-13e1b16242a6.png)


# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
The campus of UWC ISAK Japan is located in a small town on a mountain, Karuizawa. The altitude is nearly 1000m, and the humidity as well as temperature is 
lower compared to that of the sea surface ground. From SKINKRAFT LABORATORY, the low humidity and temperature causes a lot of problems such as excessive sweating, acne breakout, anhidrosis and heat rash . For that reason, Student A from UWC ISAK Japan has requested an application to be updated of local temperature and humidity, and furthermore be updated of future temperature and humidity predictions for low-cost budget. This is also going to be used to help the client decide how they dress the next day accordingly to the predicted temperature and humidity.

Source: https://skinkraft.com/blogs/articles/how-does-humidity-affect-your-skin#how-does-humidity-affect-your-skin

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

![sysdim_sl](https://user-images.githubusercontent.com/112055140/203182724-3269caac-827f-4df0-aca7-fdd1c872a1a6.png)

**Fig.1** shows the system diagram for the proposed solution (**SL**). The indoor variables will be measured using an Arduino microprocessor and the sensor DHT11 conencted to the local computer (Laptop) located inside a room. The outdoor variables will be requested to the remote server using a GET request to the API of the server at ```192.168.6.147/readings```. The local values are stored in a CSV database locally.

## Record of Tasks

|    | Planned Action                                               | Planned Outcome                                                             | Time estimate | Target completion date  | Criterion |
|----|--------------------------------------------------------------|-----------------------------------------------------------------------------|---------------|-------------------------|-----------|
| 1  | Write the problem definition                                 | To describe what is our customer problem and what is his/her situation      | 10 min        | Nov 22                  | A         |
| 2  | Read the proposed solution                                   | To have a clear idea of what we have to code to solve our customer problems | 3 min         | Nov 22                  | A         |
| 3  | Read the success criteria (SL)                               | To have a clear idea of what we have to implement in our project            | 3 min         | Nov 23                  | A         |
| 4  | Look at the system diagram                                   | To have a clear idea of how Arduino works                                   | 3 min         | Nov 23                  | A         |
| 5  | Code the program to get data of the temperature and humidity | To be able to record the temperature and the humidity of the place on 48h   | 2h            | Nov 25                  | C         |
| 6  | Set up Arduino in the computer                               | To actually record the temperature and the humidity                         | 10 min        | Dec 2                   | C         |
| 7  | Record the temperature and humidity with Arduino             | To get a database of temperature and humidity                               | 48h           | Dec 2                   | C         |
| 8  | Code the menu of the application for the customer            | To allow the customer to choose his/her options                             | 20 min        | Dec 3                   | C         |
| 9  | Code the first option of the application: get humidity       | To allow the customer to get the current humidity of the room               | 25 min        | Dec 4                   | C         |
| 10 | Code the second option of the application: get temperature   | To allow the customer to get the current temperature of the room            | 25 min        | Dec 6                   | C         |
| 11 | Code the third option of the application: exit               | To allow the customer to exit from the application when he/she is done      | 10 min        | Dec 6                   | C         |
| 12 | Print the welcome message of the application                 | To present the application to the customer                                  | 3 min         | Dec 8                   | C         |
| 13 | Code the while loop of the menu                              | To allow the customer to enter more than one option                         | 45 min        | Dec 9                   | C         |
| 14 | Add colors to the code                                       | To make the instructions more clear for the customer                        | 15 min        | Dec 9                   | C         |
| 15 | Creation of the 2 flow diagrams                              | To make the design program more understandable                              | 30 min        | Dec 10                  | B         |
| 16 | Test plan                                                    | To show to the customer how to use the application                          | 30 min        | Dec 10                  | C         |
| 17 | Record the video                                             | To show that the application is working                                     | 7 min         | Dec 11                  | D         |
| 18 | Make the science poster                                      | To explain the application to the customer with the graphs                  | 30 min        | Dec 12                  | D         |
## Test Plan

| **Software Testing:**                  | **Input:**                                                                                                                                        | **Process:**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | **Planned Outcome:**                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Functional: <br>Unit Testing           | Program to receive humidity and temperature data <br>from DHT11 sensor through the Arduino.                                                       | 1. Set up DHT11 sensor on Arduino<br>2. Connect laptop to Arduino<br>3. Run the coded program<br>4. Make visual confirmation that<br>the humidity and temperature is<br>being recorded from the DHT11 sensor<br>and put into a csv database file.                                                                                                                                                                                                                                                                                                              | The program is properly<br>processing the data gathered<br>from the DHT11 sensor into<br>a csv database file. The processing<br>is seamlessly and effectively done<br>so that it does not require additional<br>processing of the data afterwards, <br>and the data is ready for immediate use.                                                                                           |
| Functional: <br>Integration Testing    | The DHT11 sensor is acquiring accurate humidity<br>and temperature data, and sending proper data<br>to the laptop through the Arduino.            | 1. Set up the DHT11 sensor on Arduino<br>2. Connect the laptop to Arduino<br>3.1. Run the coded program in a warm room<br>and record the temperature and humidity.<br>3.2. Run the coded program outside in <br>cold weather and record the temperature<br>and humidity. <br>4. Verify that the data are accurate<br>and change accordingly to the location. <br>Ex. Warm place, cold place, humid place, etc.                                                                                                                                                 | The two different datas collected shows<br>proof that the DHT11 sensor is collecting<br>accurate humidity and temperature data. <br>Furthermore, the collection of data is <br>consistent and remains accurate. The data<br>is properly sent to the laptop without any<br>bugs. DHT11 sensor is fully functional and<br>supports the collection of data on the laptop<br>through Arduino. |
| Functional: <br>Unit Testing           | The program that graphs the humidity and temperature<br>data received from the DHT11 sensor through the<br>Arduino.                               | 1. Process humidity and temperature datas <br>into a csv database file. <br>2. Use the database file to list the mean,<br>standard deviation, maximum and minimum of<br>the collected data.<br>3. Process those values into a graph with the<br>program.                                                                                                                                                                                                                                                                                                       | The program produces and clear and an <br>easy-to-undersatnd graph from the given datas.<br>The program processes the datas correctly, and<br>does not have any malfunctions that could sabotage<br>the process.                                                                                                                                                                          |
| Non-Functional:<br>Usability Testing   | The program that receives humidity and temperature<br>data from the DHT11 sensor through the Arduino <br>writes its data in an user-friendly way. | 1. Have the DHT11 sensor and Arduino set up and<br>connected to the laptop.<br>2. Execute the program on PyCharm. <br>3. Make sure that every writes that the program <br>makes is accompanied with the date and time of <br>when the action is taken. <br>4. Confirm consistency and sustainability of <br>this program.                                                                                                                                                                                                                                      | The program produces clear and user-friendly<br>csv database file that can be immediately<br>put into use. This is achieved by an organized and<br>easy-to-understand interface produced by the program.<br>Each writes that the program makes will have date <br>and time to make it easier for the user to process<br>data afterwards.                                                  |
| Non-Functional:<br>Performance Testing | The program that receives humidity and <br>temperature data from the DHT11 sensor through <br>the Arduino executes its action every 5 minutes.    | 1. Have the DHT11 sensor and Arduino set up<br>and connected to the laptop. <br>2. Execute the program on PyCharm. <br>3. Confirm that the imported data from the DHT11<br>sensor through Arduino is written on the csv<br>database file every 5 minutes.                                                                                                                                                                                                                                                                                                      | The program demonstrates excellent performance<br>that executes every 5 minutes. The program writes<br>the collected data in the csv database file every<br>5 minutes, and produces an organized database file<br>that can be immediately put into use.                                                                                                                                   |
| Non-Functional:<br>Usability Testing   | The program that graphs the humidity and temperature<br>data received from the DHT11 sensor through the<br>Arduino.                               | 1. Process humidity and temperature datas <br>into a csv database file.<br>2. Use the database file to list the mean, <br>sstandard deviation, maximum and minimum of the<br>collected data.<br>3. Process those values into a graph with the<br>program. <br>4. Verify that the graph is easy-to-understand<br>and uses color variations to clarify different<br>values on the graph. <br>5. Each values are clearly labelled and other <br>unclear factors that could negatively impact <br>the graph is clarified through the use of <br>labels and colors. | The program produces easy-to-understand graphs that<br>is user-friendly for immediate use. The graphs produced<br>use labels and colors to make it easy for users to<br>not only understand but also put into use in a lot of ways.<br>There are no bugs found in the program, and the graphs<br>maintain a solid quality regardless of the quality of<br>the collected data.             |
# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
