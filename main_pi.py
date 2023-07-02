import serial
import time

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    if isinstance(data, int):
        byte_data = data.to_bytes(2, byteorder='big')  # Convert integer to 2-byte representation
    elif isinstance(data, str):
        byte_data = data.encode()  # Convert string to byte
    try:
        serial_port.write(byte_data)
        print("Data sent successfully:", byte_data)
    except Exception as e:
        print("Error sending data:", str(e))
    time.sleep(0.01)


# Example usage
if __name__ == "__main__":
    send_data(1024)
