"""
This module implements a virtual class representing a physical Component connected to the Raspberry through a number of Pins. The class Component is not meant to be used directly but is to be inherited from by specific Component types (LED, buttons, shields, ...).
"""

class Component(object):
    """Virtual component class. Holds things common to all components

    Attributes:
        name (str): name of the Component
        type (str): meant for info such as input/output/...
        GPIOs (:obj:`dict` of :obj:`Pin`): dictionary of Pin ojects

    Methods:
        update: meant to check and update status.
        call: meant to do the main action associated with an active component
        get/setitem: access the GPIOs dictionnary

    Notes:
        Pins can be inappropriately setup: there is no check that several Pin objects are created for the same physical
        pin, even within the same Component.
        TODO: A PinManager is available in the HardwareManager class that ensures that
        there are no conflicts.
    """

    def __init__(self, name, *args, **kwargs):
        """Basic initialization of a virtual component

        Args:
            name: (str)
        Keyword Args
            type: (str) this should be "virtual" for a Component` but the type edition option is exposed here for child classes`
        """
        try:
            self.name = str(name)
        except TypeError:
            raise TypeError("A Component's name has to be a string")

        if "type" in kwargs:
            try:
                self.type = kwargs["type"]
            except TypeError:
                raise TypeError("A Component's type has to be a string")
        else:
            self.type = "virtual"
        self.GPIOs = {}

    def update(self, ignore=True, *args, **kwargs):
        """Collect the status of input Pins and whatever data is available.

        In this virtual class, a NotImplemented Error is raised by default since it should do nothing.

        Args:
            ignore (bool): if True, ignore this component when called and do not raise an error if it is not callable
        """
        if ignore:
            pass
        else:
            raise NotImplementedError("This Component is not updatable. It can be safely called using the ignore=True option.")

    def __getitem__(self, item):
        """Access the component's GPIO dictionnary

        Args:
            item: key that references a Pin of the Component. Should have a meaningful name relating to the Component's physical I/O

        Returns:
            the Pin referenced by this pin
        """
        try:
            p = self.GPIOs[item]
        except KeyError:
            raise KeyError("The Component object "+self.name+" has no Pin referenced as "+str(item))
        return p

    def __setitem__(self, key, value):
        """Set an element in the component's GPIO dictionnary

        Args:
            key: key that references a Pin of the Component. Should have a meaningful name relating to the Component's physical I/O
            value (Pin): the corresponding Pin object corresponding
        """
        self.GPIOs[key] = value