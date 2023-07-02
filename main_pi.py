import serial

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    try:
        serial_port.write(data)
        print("Data sent successfully:", data)
    except Exception as e:
        print("Error sending data:", str(e))

# Example usage
send_data(1024)
