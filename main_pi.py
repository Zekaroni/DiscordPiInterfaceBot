from serial import Serial

try:
    # Create a serial object with the appropriate port and baud rate settings
    ser = Serial('/dev/serial1', 9600)

    # Send a byte of data to the Arduino
    data_byte = 0x41  # Byte value to send
    ser.write(data_byte)

    # Close the serial connection
    ser.close()
except Exception as e:
    print("Serial communication error:", str(e))

    
