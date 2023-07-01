import RPi.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pin (using physical pin numbers)
gpio_pin = 11  # Pin 11 (GPIO17)

# Set up the GPIO pin
GPIO.setup(gpio_pin, GPIO.OUT)

# Send data to Arduino
data = b'H'

# Send each bit of the data sequentially
for bit in data:
    print(bit)
    for i in range(8):
        GPIO.output(gpio_pin, bit & (1 << i))
        time.sleep(0.01)  # Adjust the delay as needed

# Clean up the GPIO pin
GPIO.cleanup()
