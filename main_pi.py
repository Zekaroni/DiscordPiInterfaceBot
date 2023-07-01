import serial

try:
    # Create a serial object with the appropriate port and baud rate settings
    ser = serial.Serial('/dev/serial1', 9600)

    # Send a byte of data to the Arduino
    data_byte = b'\x41'  # Byte value to send
    ser.write(data_byte)

    # Close the serial connection
    ser.close()
except Exception as e:
    print("Serial communication error:", str(e))
