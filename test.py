from serial import Serial
from struct import pack as struct_pack
from time import sleep

class SerialOutput:
    def __init__(self,
        port="/dev/ttyS0",
        baudrate=9600,
        timeout = 1,
        debug = False):
        self._serial_port = Serial(port, baudrate=baudrate, timeout=timeout)
        self._debug = debug

    def send_data(self, data):
        try:
            packed_data = struct_pack('>I', data)
            self._serial_port.write(packed_data)
            if self._debug:
                print("Data sent successfully:", packed_data.hex())  # Convert packed_data to hex string
        except Exception as e:
            if self._debug:
                print("Error sending data:", str(e))

if __name__ == "__main__":
    SendClient = SerialOutput()

    print("Now sending data with wrong verification:")
    SendClient.send_data(0b1011100011111111) # Setting motor 1 to max speed, but should fail
    sleep(5)
    print("Data was sent, if motor didn't turn on, test passed\n\n")
    sleep(2)

    print("Now turning on motor 1, none others should turn on.")
    SendClient.send_data(0b1010100011111111) # Max speed on motor 1
    sleep(5)

    print("Now turning on motor 2, none others should turn on.")
    SendClient.send_data(0b1010101011111111) # Max speed on motor 2
    sleep(5)

    print("Now turning on motor 3, none others should turn on.")
    SendClient.send_data(0b1010110011111111) # Max speed on motor 2
    sleep(5)


    print("Now turning on motor 4, none others should turn on.")
    SendClient.send_data(0b1010111011111111) # Max speed on motor 2
    sleep(5)

    print("Now turning off motor 1. (NOTE: there should be no humming from the motor)")
    SendClient.send_data(0b1010100000000000) # Motor 1 off
    sleep(2)

    print("Now turning off motor 2. (NOTE: there should be no humming from the motor)")
    SendClient.send_data(0b1010101000000000) # Motor 2 off
    sleep(2)

    print("Now turning off motor 3. (NOTE: there should be no humming from the motor)")
    SendClient.send_data(0b1010110000000000) # Motor 2 off
    sleep(2)

    print("Now turning off motor 4. (NOTE: there should be no humming from the motor)")
    SendClient.send_data(0b1010111000000000) # Motor 2 off
    sleep(2)


    print("Testing has finished")