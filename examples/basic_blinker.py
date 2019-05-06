from hardware_manager.manager import HardwareManager
from hardware_manager.components.output.led import LED_blink

H = HardwareManager()
LB = LED_blink("blinker",21)
H.add_component(LB)

def blink():
    H['blinker'].start_running()
    t0 = H.current_milli_time()
    do_print = True
    while H.current_milli_time()-t0<5000:
        H.update()
        if (H.current_milli_time()-t0)%100 == 0:
            if do_print:
                print "Time elapsed: {}".format(H.current_milli_time()-t0)
                print "Blinker LED status: {}\n".format(H['blinker']())
                do_print = False
        else:
            do_print = True

    H['blinker'].stop_running()