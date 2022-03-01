from robotpwm import RobotWithPWM
import time

robot = RobotWithPWM();

# Move forward for 5 secs
robot.forward(speed=10)
time.sleep(1)
robot.right(speed=10)
time.sleep(1)
robot.reverse(speed=10)
time.sleep(1)
robot.left(speed=10)
time.sleep(1)
robot.stop()

