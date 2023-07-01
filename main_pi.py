import serial

# Configure serial communication
serial_port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    serial_port.write(data.encode())

# Example usage
send_data("Hello, Arduino!")
