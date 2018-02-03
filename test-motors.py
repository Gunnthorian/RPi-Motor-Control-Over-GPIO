import RPi.GPIO as GPIO
import time

''' This is the initialization for GPIO stuff '''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

''' This is the setup for every motor on the robot '''
GPIO.setup(17, GPIO.OUT)

motor_1 = GPIO.PWM(17, 50)

motor_1.start(3)

''' This is the code for the robot '''

while True:

    duty_cycle = raw_input('Duty Cycle: ')
    motor_1.ChangeDutyCycle(float(duty_cycle))
    print 'Duty Cycle set to ', duty_cycle
