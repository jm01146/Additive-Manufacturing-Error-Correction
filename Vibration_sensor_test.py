import serial
import time
#from mpu6050 import mpu6050

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser2 = serial.Serial("/dev/ttyACM1", 9600, timeout=1)
#mpu = mpu6050(0x68)

vibe = open("vibration_FIU_Logo", "a")
curry = open("current_FIU_Logo.csv", "a")
#gyro_x = open("gryo_x_FIU_Logo_v1.csv", "a")
#gyro_y = open("gryo_y_FIU_Logo_v1.csv", "a")
#gyro_z = open("gryo_z_FIU_Logo_v1.csv", "a")
#accel_x = open("accel_x_FIU_Logo_v1.csv", "a")
#accel_y = open("accel_y_FIU_Logo_v1.csv", "a")
#accel_z = open("accel_z_FIU_Logo_v1.csv", "a")

t_end = 20
time.sleep(2)

for x in range(t_end):
    time.sleep(1)
    for i in range(100):
        line = ser.readline()
        line2 = ser2.readline()
        #accel_data = mpu.get_accel_data()
        #gyro_data = mpu.get_gyro_data()
        if line2:
            string = line.decode()
            string2 = line2.decode()
            data = int(string2)
            vibe.write(str(string) + "\n")
            curry.write(str(data) + "\n")
            #accel_x.write(str(accel_data['x']) + "\n")
            #accel_y.write(str(accel_data['y']) + "\n")
            #accel_z.write(str(accel_data['z']) + "\n")
            #gyro_x.write(str(gyro_data['x']) + "\n")
            #gyro_y.write(str(gyro_data['y']) + "\n")
            #gyro_z.write(str(gyro_data['z']) + "\n")
            print(str(string2))
            
vibe.close()
curry.close()
#accel_x.close()
#accel_y.close()
#accel_z.close()
#gyro_x.close()
#gyro_y.close()
#gyro_z.close()
ser.close()
ser2.close()