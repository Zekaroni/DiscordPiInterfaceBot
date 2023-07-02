import serial
import time

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

def send_data(data):
    try:
        # Create a bytearray with the four bytes in little-endian order
        byte_data = bytearray([data & 0xFF, (data >> 8) & 0xFF, (data >> 16) & 0xFF, (data >> 24) & 0xFF])

        # Send the bytearray to the Arduino
        serial_port.write(byte_data)
        print("Data sent successfully:", byte_data)
    except Exception as e:
        print("Error sending data:", str(e))
    time.sleep(0.01)

# Example usage
if __name__ == "__main__":
    send_data(0xFF00003E)
