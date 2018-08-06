class VirtualComponent(object):
    """Virtual component class. Holds things common to all components"""
    def __init__(self,name,*args,**kwargs):
        self.name=name
        self.type="virtual"
        self.GPIOs={}

    def update(self,*args,**kwargs):
        return NotImplemented

    def __call__(self, *args, **kwargs):
        return NotImplemented

    def __getitem__(self, item):
        return self.GPIOs[item]

    def __setitem__(self, key, value):
        self.GPIOs[key]=value






