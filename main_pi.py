import serial
import struct
import time

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

def send_data(data):
    try:
        # Send the four bytes individually to the Arduino
        serial_port.write((data >> 24) & 0xFF)
        serial_port.write((data >> 16) & 0xFF)
        serial_port.write((data >> 8) & 0xFF)
        serial_port.write(data & 0xFF)
        print("Data sent successfully:", hex(data))
    except Exception as e:
        print("Error sending data:", str(e))
    time.sleep(0.01)

# Example usage
if __name__ == "__main__":
    send_data(0xFF00003E)
