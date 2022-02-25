# Install Jetson GPIO
# 32 and 33 are the PWM pins (Board pin numbers on Jetson)
# Connect them to L293D (A1, B1 and do trials accordingly)
# Use 36 and 37 for reverse motion, 26 is right reverse, 37 is left reverse

# Whenever you move 32 and 33 to LOW, it remains as it is. So use start function

import time
import Jetson.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Robot:
    def __init__(self):
        self.direction="Forward"
        self.left_motor = [32, 36]
        self.right_motor = [33, 37]
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)

    def forward(self):
        self.direction="Moving forward"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        print(self.direction)

    def right(self):
        self.direction="Moving right"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.LOW)
        GPIO.output(self.right_motor[1], GPIO.LOW)
        print(self.direction)

    def stop(self):
        self.direction="Stopped"
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        print(self.direction)
    def start(self):
        self.direction="Started"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        print(self.direction)

    def left(self):
        self.direction="Moving left"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        print(self.direction)

    def reverse(self):
        self.direction="Moving reverse"
        GPIO.output(self.left_motor[0], GPIO.LOW)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        GPIO.output(self.left_motor[1], GPIO.HIGH)
        GPIO.output(self.right_motor[1], GPIO.HIGH)
        print(self.direction)