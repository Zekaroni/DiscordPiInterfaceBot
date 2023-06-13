import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# TODO: Idea list
# Add a way to visualize which pins are being used
# Add a way to get  notified when a pin changes states from HIGH/LOW when it is INPUT
# 
# 
class Pin:
    def __init__(self) -> None:
        self.isActive = False
        self.isBanned = False
        self.isWatched = False


class Device:
    def __init__(self):
        self.pins = []
        self._banned_pins = [
            3,    # Pull-up resistor, can be used for input
            5,    # Pull-up resistor, can be used for input
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
            40,   # Reserved, imposible to index with bot
        ]

        for i in range(40):
            self.pins.append(Pin())
            if (i+1) in self._banned_pins:
                self.pins[i].isBanned = True

    def setup_pin(self, pin_num, pin_out) -> None:
        """
        param pin_num: The number of the pin on the board
        param pin_out: True if you want pin output, False for pin input
        """
        pin_index = pin_num-1
        if not self.pins[pin_index].isBanned:
            if not self.pins[pin_index].isActive:

                # Enables the pin to be accesed by the GPIO API
                GPIO.setup(pin_num, (GPIO.OUT if pin_out else GPIO.IN))
                self.pins[pin_index].isActive = True

            else:
                raise ConnectionError(f"Pin {pin_num} is already active.")
        else:
            raise PermissionError(f"Pin {pin_num} has been restricted by host, choose another pin.")
        

    def set_pin_high(self,pin_num) -> None:
        pin_index = pin_num-1
        if self.pins[pin_index].isBanned:
            raise("Pin {pin_num} has been restricted by host. Unable to turn it on.")
        if self.pins[pin_index].isActive:
            GPIO.output(pin_num, GPIO.HIGH)
        else:
            raise ("Pin has not been setup.")
        

    @staticmethod
    def get_cpu_temperature() -> float:
        with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
            temp = round(int(f.read().strip()) / 1000.0,1)
        return temp

    @staticmethod
    def get_gpu_temperature() -> str:
        return subprocess.check_output("vcgencmd measure_temp", shell=True).decode("utf-8").replace('temp=','').replace("'C\n",'')
