import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


class Device:
    def __init__(self):
        self._active_pins = [] # For pins that get activated

        self._banned_pins = [
            3,    # Pull-up resistor, input
            5,    # Pull-up resistor, input
            13,   # Reserved
            19,   # Reserved
            21,   # Reserved
            23,   # Reserved
            24,   # Reserved
            27,   # ID EEPROM
            28,   # ID EEPROM
            29,   # ID EEPROM
            31,   # Reserved
            33,   # Reserved
            35,   # Reserved
            37,   # Reserved
            38,   # Reserved
            40,   # Reserved
        ]

    def setup_pin(self, pin_num, pin_out) -> None:
        """
        param pin_num: The number of the pin on the board
        param pin_out: True if you want pin output, False for pin input
        """
        if pin_num < 0 or pin_num > 40:
            raise ValueError("Enter a pin from 1-40")
        if pin_num not in self._banned_pins:
            if pin_num not in self._active_pins:
                GPIO.setup(pin_num, GPIO.OUT if pin_out is True else GPIO.IN)
                self._active_pins.append(pin_num)
            else:
                raise ConnectionError(f"Pin {pin_num} is already active.")
        else:
            raise PermissionError(f"Pin {pin_num} has been restricted by host, chose another pin.")

    @staticmethod
    def get_cpu_temperature() -> float:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = round(int(f.read().strip()) / 1000.0,1)
        return temp

    @staticmethod
    def get_gpu_temperature() -> str:
        return subprocess.check_output("vcgencmd measure_temp", shell=True).decode("utf-8").replace('temp=','').replace("'C\n",'')
