import serial

# Configure serial communication
serial_port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Send data to Arduino
def send_data(data):
    if isinstance(data, int):
        print([data])
        print(bytes([64]))
        data = bytes([data])  # Convert integer to byte
    elif isinstance(data, str):
        data = data.encode()  # Convert string to byte
    try:
        serial_port.write(data)
        print("Data sent successfully:", data)
    except Exception as e:
        print("Error sending data:", str(e))

# Example usage
send_data(2147483647)
