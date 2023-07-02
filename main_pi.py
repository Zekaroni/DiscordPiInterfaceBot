import serial
import time

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    if type(data) == bin():
        serial_port.write(data)
    else:
        try:
            serial_port.write(data.encode())
            print("Data sent successfully:", data)
        except Exception as e:
            print("Error sending data:", str(e))
    try:
        serial_port.write(data)
        print("Data sent successfully:", data)
    except Exception as e:
        print("Error sending data:", str(e))
    time.sleep(0.3)

# Example usage
if __name__ == "__main__":
    send_data(1024)
