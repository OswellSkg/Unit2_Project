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
