from robot import Robot
import time

robot = Robot();

# Move forward for 5 secs
robot.forward()
time.sleep(1)
robot.right()
time.sleep(1)
robot.reverse()
time.sleep(1)
robot.left()
time.sleep(1)
robot.stop()

