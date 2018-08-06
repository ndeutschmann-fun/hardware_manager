class VirtualComponent(object):
    """Virtual component class. Holds things common to all components
    Attributes:
        * name
        * type: meant for input/output
        * GPIOs dictionnary to access the Pin objects
    Methods:
        * update: meant to check and update status.
        * call: meant to do the main action associated with an active component
        * get/setitem: access the GPIOs dictionnary
    """
    def __init__(self,name,*args,**kwargs):
        self.name=name
        self.type="virtual"
        self.GPIOs={}

    def update(self,*args,**kwargs):
        """update should be implemented for EVERY component so as not to have error
        during the end of loop update.
        """
        pass

    def __call__(self, *args, **kwargs):
        """Do the main action associated to the component"""
        return NotImplemented

    def __getitem__(self, item):
        """Access the component's GPIO dictionnary"""
        return self.GPIOs[item]

    def __setitem__(self, key, value):
        """Set an element in the component's GPIO dictionnary
        Note: no check is performed that the `value` is actually a Pin"""
        self.GPIOs[key]=value






