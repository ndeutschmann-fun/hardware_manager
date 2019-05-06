import time

from hardware_manager.RPi import GPIO


class HardwareManager(object):
    """A class that handles a list of harware elements
    Attributes are:
    * name: the name of the manager
    * mode: the GPIO mode
    * components: a dictionnary of Components, accessed by name
    * last_update: the time since the last call of self.update()
    """

    @staticmethod
    def current_milli_time():
        """return the current time since epoch in miliseconds"""
        return int(round(time.time() * 1000))

    def __init__(self, component_list=[], name="HM", mode=GPIO.BCM, *args, **opts):
        """Optional arguments:
        * Component object list
        * name for the Manager
        * GPIO board mode to access the Pins
        """
        self.last_update= self.current_milli_time()
        self.mode=mode
        GPIO.setmode(mode)
        self.name=name
        self.components = {}
        for component in component_list:
            self.add_component(component)

    def add_component(self,component):
        """Add a Component in the Manager component list."""
        if component.name in self.components:
            raise NameError("This component name is already used in Hardware Manager "+self.name+"")
        else:
            self.components[component.name]=component

    def update(self):
        """Update all components. Pass delay since last check to components"""
        dt = self.current_milli_time() - self.last_update
        self.last_update += dt
        for component in self.components.values():
            component.update(delay=dt)

    def cleanup(self):
        GPIO.cleanup()


    def __getitem__(self, item):
        return self.components[item]