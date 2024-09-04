# This file is for another error detection project with FIU BIO-MEMS Lab
# This is testing how the mpu6050 works to integrate it to other projects
from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

while True:

    
    accel_data = mpu.get_accel_data()
    print("Acc X : " + str(accel_data['x']))
    print("Acc Y : " + str(accel_data['y']))
    print("Acc Z : " + str(accel_data['z']))
    print()
    
    gyro_data = mpu.get_gyro_data()
    print("Gyro X : " + str(gyro_data['x']))
    print("Gyro Y : " + str(gyro_data['y']))
    print("Gyro Z : " + str(gyro_data['z']))
    print()
    print("-----------------------------------")
    time.sleep(1)
    
    g = open("data_gyro_test.csv", "a")
    a = open("data_accel_test.csv", "a")
    
    a.write(str(accel_data['x']))
    a.write('\n')
    a.write(str(accel_data['y']))
    a.write('\n')
    a.write(str(accel_data['z']))
    a.write('\n')
    g.write(str(gyro_data['x']))
    g.write('\n')
    g.write(str(gyro_data['y']))
    g.write('\n')
    g.write(str(gyro_data['z']))
    g.write('\n')
    
    a.close()
    g.close()
