from machine import Pin, PWM, disable_irq, enable_irq
import time 
from simplemotordriver import Simplemotordriver

class Piston:
    def __init__(self, in1_pin, in2_pin):
        # Motor Driver Setup from Arguments
       
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.pwm1 = PWM(self.in1)
        self.pwm2 = PWM(self.in2)
        self.pwm1.freq(500)
        self.pwm2.freq(500)
        #stop the motor hard
        self.pwm1.duty(1023)
        self.pwm2.duty(1023)
        
    def motgo(self, speed):

        pwm_value = int(min(max(abs(speed), 0), 100) * 10.23)  # Map -100 to 100 to 0 to 1023
        pwm_value = max(0, min(pwm_value, 1023))

        #print('speed pwm value = ', pwm_value)
        if speed > 0:
            # Forward direction
            print("Motor forward at", pwm_value)
            self.pwm1.duty(pwm_value)
            self.pwm2.duty(0)
        elif speed < 0:
            # Reverse direction
            self.pwm1.duty(0)
            self.pwm2.duty(pwm_value)
        else:
            # Stop the motor
                self.stop()

            
    def stop(self):
        self.pwm1.duty(0)
        self.pwm2.duty(0)
        
    def demo(self):
        for spd in [50, -50, 0]:
            self.motgo(spd)
            time.sleep(1)
