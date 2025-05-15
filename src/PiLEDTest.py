import hal.hal_input_switch as switch
import hal.hal_led as led
import time
from time import sleep


def main():
    led.init()
    switch.init()
    loop()
    
    
def loop():
    thing = 0
    fist = True
    while(True):
        if switch.read_slide_switch():
            for i in range(0, 50, 1):
                if not switch.read_slide_switch() or fist == False:
                    break
                time.sleep(0.1)
                thing = 1 if thing == 0 else 0
                led.set_output(1, thing)
            fist = False
            led.set_output(1, 0)
        else:
            fist = True
            time.sleep(0.2)
            thing = 1 if thing == 0 else 0
            led.set_output(1, thing)


if __name__ == "__main__":
    main()


