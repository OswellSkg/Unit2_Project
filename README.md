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

| Task Nomber | Planned Action                                               | Planned Outcome                                                             | Time estimate | Target completion date  | Criterion |
|-------------|--------------------------------------------------------------|-----------------------------------------------------------------------------|---------------|-------------------------|-----------|
|             |                                                              |                                                                             |               |                         |           |
| 1           | Write the problem definition                                 | To describe what is our customer problem and what is his/her situation      | 10 min        | Nov 22                  | A         |
| 2           | Read the proposed solution and success criteria              | To have a clear idea of what we have to code to solve our customer problems | 3 min         | Nov 22                  | A         |
| 3           | Code the program to get data of the temperature and humidity | To be able to record the temperature and the humidity of the place on 48h   | 2h            | Nov 25                  | C         |
| 4           | Record the temperature and humidity with Arduino             | To get a database of temperature and humidity                               | 48h           | dec 2                   | D         |
| 5           | Record the temperature and humidity with Arduino             | To get a database of temperature and humidity                               | 48h           | dec3                    | D         |
| 6           | Record the temperature and humidity with Arduino             |                                                                             |               |                         |           |
## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
