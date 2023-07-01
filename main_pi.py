import serial
import time

serial_port = '/dev/serial1' 
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

time.sleep(2)

ser.write('H'.encode())

ser.close()