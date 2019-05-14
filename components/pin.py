from hardware_manager.RPi import GPIO

class Pin(object):
    """Representation of a physical pin on the board"""
    def __init__(self, pin_number, mode=GPIO.IN, delay=1e-3, initial_state=GPIO.LOW, pull_up_down=GPIO.PUD_UP, activate=True, *args, **kwargs):
        self.pin=pin_number
        self.mode=mode
        self.state=initial_state
        self.pull_up_down=pull_up_down
        if activate:
            GPIO.setup(self.pin, mode, pull_up_down=self.pull_up_down)
            if self.mode == GPIO.OUT:
                GPIO.output(self.pin, initial_state)
                self.flip = self.OUT_flip
                self.high = self.OUT_high
                self.low = self.OUT_low
            else:
                self.state = GPIO.input(self.pin)
                self.flip = self.not_output
                self.high = self.not_output
                self.low = self.not_output

    def not_output():
        """Trying to set the state of an input pin should return an error"""
        raise TypeError("This pin is an INPUT pin: "+str(self.pin))

    def OUT_flip(self):
        """Flip the status of an output pin"""
        self.state= not self.state
        GPIO.output(self.pin, self.state)

    def OUT_high(self):
        self.state = GPIO.HIGH
        GPIO.output(self.pin, self.state)

    def OUT_low(self):
        self.state= GPIO.LOW
        GPIO.output(self.pin, self.state)

    def update(self):
        self.state = GPIO.input(self.pin)