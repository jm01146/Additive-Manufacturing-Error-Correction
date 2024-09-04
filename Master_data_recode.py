import time
import serial
import threading
#from mpu6050 import mpu6050

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser2 = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
#mpu = mpu6050(0x68)

vibe = open("vibe_test.csv", "a")
cur = open("current_test.csv", "a")
#gyro_x = open("gryo_x_test.csv", "a")
#gyro_y = open("gryo_y_test.csv", "a")
#gyro_z = open("gryo_z_test.csv", "a")
#accel_x = open("accel_x_test.csv", "a")
#accel_y = open("accel_y_test", "a")
#accel_z = open("accel_z_test", "a")

t_end = 20
time.sleep(2)

def recording_one():
    global ser
    global t_end
    global vibe
    for x in range(t_end):
        time.sleep(1)
        for i in range(100):
            line = ser.readline()
            if line:
                string = line.decode()
                vibe.write(str(string) + "\n")
                #print(str(string))


def recording_two():
    global ser2
    global t_end
    global cur
    for x in range(t_end):
        time.sleep(1)
        for i in range(100):
            line = ser2.readline()
            if line:
                string = line.decode()
                cur.write(str(string) + "\n")
                print(str(string))
                print('nada')
  
  
#def recording_three():
    #global t_end
    #global mpu
    #global gyro_x
    #global gyro_y
    #global gyro_z
    #global accel_x
    #global accel_y
    #global accel_z
    
    #for x in range(t_end):
        #time.sleep(1)
        #for i in range(100):
            #accel_data = mpu.get_accel_data()
            #gyro_data = mpu.get_gyro_data()
            #if accel_data:
                #accel_x.write(str(accel_data['x']) + "\n")
                #accel_y.write(str(accel_data['y']) + "\n")
                #accel_z.write(str(accel_data['z']) + "\n")
                #gyro_x.write(str(gyro_data['x']) + "\n")
                #gyro_y.write(str(gyro_data['y']) + "\n")
                #gyro_z.write(str(gyro_data['z']) + "\n")

Thread1 =threading.Thread(target=recording_one)
Thread2 =threading.Thread(target=recording_two)
#Thread3 =threading.Thread(target=recording_three)

Thread1.start()
Thread2.start()
#Thread3.start()
Thread1.join()
Thread2.join()
#Thread3.join()

print('Recording is done <3')

vibe.close()
cur.close()
#accel_x.close()
#accel_y.close()
#accel_z.close()
#gyro_x.close()
#gyro_y.close()
#gyro_z.close()
ser.close()
ser2.close()