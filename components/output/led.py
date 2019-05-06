"""Implementation of the LED classes
Available classes:

LED: the most basic output class possible TODO

LED_blink: a slight extension with a blinking option at a given frequency TODO

LED_program: a LED with a blinking program TODO

"""


import hardware_manager.components.virtual_component as virtual_component
import hardware_manager.components.pin as pin


class LED(virtual_component.Component):
    """A LED that can be turned on or off"""
    def __init__(self, name, pin_id, initial_state=pin.GPIO.LOW, activate=True):
        """Creator for a basic LED

        Args:
            name:
            pin_id:
            initial_state:
            activate:
        """
        virtual_component.Component.__init__(self, name, type="LED")
        self[0] = pin.Pin(pin_id, mode=pin.GPIO.OUT, initial_state=initial_state, activate=activate)

    def on(self):
        """Turn the LED on"""
        self[0].high()

    def off(self):
        """Turn the LED off"""
        self[0].low()

    def switch(self):
        """Flip the LED"""
        print "flipping led"
        self[0].flip()

    def update(self, ignore=True, *args, **kwargs):
        """No need to update basic leds"""
        pass

    def __call__(self):
        """Return the current status"""
        return self[0].state

class LED_blink(LED):
    """A LED that blinks with a given period"""
    def __init__(self,name, pin_id, period=1000 , initial_state=False, activate=True):
        """Creator for a blinking light

        Args:
            name:
            pin_id:
            period: period in ms
            initial_state:
            activate:
        """
        LED.__init__(self,name, pin_id, initial_state=pin.GPIO.LOW, activate=True)
        self.period = period
        self.status = activate
        self.time_elapsed = 0.
        self.running = initial_state
        if self.running:
            self.on()
        else:
            self.off()

    def update(self,delay=0.):
        """Get the time since the last call from the manager and flip the LED if necessary"""
        if self.running:
            self.time_elapsed+=delay
            if self.time_elapsed>self.period:
                self.switch()
                self.time_elapsed=0

    def start_running(self):
        "Start blinking"
        self.running = True

    def stop_running(self):
        "Stop blinking"
        self.running = False

    def toggle_running(self):
        "Toggle running mode"
        self.running = not self.running