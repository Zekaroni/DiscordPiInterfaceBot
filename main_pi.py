from serial import Serial

# Create a serial object with the appropriate port and baud rate settings
ser = Serial('/dev/serial0', 9600)

# Send a byte of data to the Arduino
data_byte = 0x41  # Byte value to send
ser.write(data_byte)

# Close the serial connection
ser.close()
