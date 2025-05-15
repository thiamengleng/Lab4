import hal.hal_input_switch as switch
import hal.hal_led as led
import time
from time import sleep


def main():
    led.init()
    switch.init()
    loop()
    
    
thing = 0
def loop():
    global thing
    while(True):
        if switch.read_slide_switch():
            time.sleep(0.1)
            thing = 1 if thing == 0 else 0
            led.set_output(1, thing)
        else:
            time.sleep(0.2)
            thing = 1 if thing == 0 else 0
            led.set_output(1, thing)


if __name__ == "__main__":
    main()


