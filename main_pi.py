import serial
from time import sleep

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    try:
        serial_port.write(data)
        print("Data sent successfully:", data)
    except Exception as e:
        print("Error sending data:", str(e))
    sleep(0.01)

# Example usage
if __name__ == "__main__":
    send_data(1024)
