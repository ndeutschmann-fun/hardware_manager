"""The Raspberry Pi python Library
If we run on an actual RPi, use the native GPIO library.
Otherwise, we use the internal GPIO_mockup
"""

import os
if os.uname()[4].startswith("arm"):
    # We are on a Rpi
    from RPi import GPIO
else:
    # We are not on a RPi, use the mockup
    from . import GPIO_mockup as GPIO

def check_GPIO():
    """Check which GPIO Library is being used"""
    print(GPIO.__name__)