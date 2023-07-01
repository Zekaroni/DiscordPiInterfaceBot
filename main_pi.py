import serial
import time

# Define the serial port and baud rate
serial_port = '/dev/serial1'  # Raspberry Pi's Serial1 port
baud_rate = 9600

try:
    # Initialize the serial connection
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print("Serial connection established!")

    # Wait for the Arduino to reset (if necessary)
    time.sleep(2)

    # Send data to Arduino
    data = 'H'
    ser.write(data.encode())
    print("Data sent to Arduino:", data)

    # Close the serial connection
    ser.close()
    print("Serial connection closed.")
except serial.SerialException as e:
    print("Serial connection failed:", str(e))
