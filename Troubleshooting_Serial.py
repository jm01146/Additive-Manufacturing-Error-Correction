# This file is for another error detection project with FIU BIO-MEMS Lab
# This is the communication portion of the code
import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
vibe = open("shoot.csv", "a")

t_end = 10
time.sleep(2)

for x in range(t_end):
    time.sleep(1)
    for i in range(100):
        line = ser.readline()
        if line:
            string = line.decode()
            data = int(string)
            vibe.write(str(data))
            print(data)
            
vibe.close()
ser.close()
