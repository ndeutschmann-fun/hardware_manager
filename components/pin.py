import ...RPi.GPIO as GPIO

class Pin(object):
    """Representation of a physical pin on the board"""
    def __init__(self,pin_number,mode=GPIO.IN,delay=1e-3,inital_state=GPIO.LOW,pull_up_down=GPIO.PUD_UP,activate=True,*args,**kwargs):
        self.pin=pin_number
        self.mode=mode
        self.state=inital_state
        self.pull_up_down=pull_up_down
        if activate:
            GPIO.setup(self.pin,mode,pull_up_down=self.pull_up_down)
            if self.mode == GPIO.OUT:
                GPIO.output(self.pin,inital_state)
            else self.state=GPIO.input(self.pin)
