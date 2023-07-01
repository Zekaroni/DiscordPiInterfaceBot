import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# Define the software serial pins
rx_pin = 17  # GPIO17 (pin 11)
tx_pin = 27  # GPIO27 (pin 13)

# Set up the GPIO pins
GPIO.setup(rx_pin, GPIO.IN)
GPIO.setup(tx_pin, GPIO.OUT)

# Define the serial port and baud rate
serial_port = serial.Serial(port='/dev/ttyS0', baudrate=9600)

try:
    # Open the serial port
    serial_port.open()
    print("Serial connection established!")

    # Send data to Arduino
    data = 'H'
    serial_port.write(data.encode())
    print("Data sent to Arduino:", data)

    # Close the serial port
    serial_port.close()
    print("Serial connection closed.")
except serial.SerialException as e:
    print("Serial connection failed:", str(e))
finally:
    # Clean up the GPIO pins
    GPIO.cleanup()
