# Install Jetson GPIO
# 32 and 33 are the PWM pins (Board pin numbers on Jetson)
# Connect them to L293D (A1, B1 and do trials accordingly)
# Use 36 and 37 for reverse motion, 26 is right reverse, 37 is left reverse

# Whenever you move 32 and 33 to LOW, it remains as it is. So use start function

import time
import Jetson.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class RobotWithPWM:
    def __init__(self):
        self.direction="Forward"
        self.left_motor = [32, 36]
        self.right_motor = [33, 37]
        self.left_speed = 0
        self.right_speed = 0
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        self.pwm = [GPIO.PWM(32, 50), GPIO.PWM(33, 50)]
        GPIO.setup(self.left_motor[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.right_motor[0], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.left_motor[1], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.right_motor[1], GPIO.OUT, initial=GPIO.LOW)
        self.pwm[0].start(0)
        self.pwm[1].start(0)

    def set_motors(self, left_speed=1.0, right_speed=1.0):
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        self.left_speed = ((left_speed - (-1)) / 2) * 100
        self.right_speed = ((right_speed - (-1)) / 2) * 100
        print()
        print()
        self.pwm[0].ChangeDutyCycle(self.left_speed)
        self.pwm[1].ChangeDutyCycle(self.right_speed)

    def forward(self, speed=1.0, duration=None):
        self.direction="Moving forward"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)
        self.pwm[0].start(0)
        self.pwm[1].start(0)
        self.pwm[0].ChangeDutyCycle(speed)
        self.pwm[1].ChangeDutyCycle(speed)
        print(self.direction)

    def right(self, speed=1.0):
        self.direction="Moving right"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)
        self.pwm[0].ChangeDutyCycle(speed)
        self.pwm[1].ChangeDutyCycle(speed)
        print(self.direction)

    def stop(self):
        self.direction="Stopped"
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        self.pwm[0].stop()
        self.pwm[1].stop()
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)
        print(self.direction)

    def start(self):
        self.direction="Started"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)
        self.pwm[0].start(0)
        self.pwm[1].start(0)
        print(self.direction)

    def left(self, speed=1.0):
        self.direction="Moving left"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        self.pwm[0].ChangeDutyCycle(speed)
        self.pwm[1].ChangeDutyCycle(speed)
        print(self.direction)

    def reverse(self, speed=1.0):
        self.direction="Moving reverse"
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.HIGH)
        GPIO.output(self.right_motor[1], GPIO.HIGH)
        self.pwm[0].ChangeDutyCycle(speed)
        self.pwm[1].ChangeDutyCycle(speed)
        print(self.direction)