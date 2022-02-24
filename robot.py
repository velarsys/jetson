import time
import Jetson.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Robot:
    def __init__(self):
        self.direction="Forward"
        self.left_motor = [32, 36]
        self.right_motor = [33, 38]
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)

    def forward(self):
        self.direction="Moving forward"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.HIGH)
        print(self.direction)

    def right(self):
        self.direction="Moving right"
        GPIO.output(self.left_motor[0], GPIO.HIGH)
        GPIO.output(self.right_motor[0], GPIO.LOW)
        print(self.direction)