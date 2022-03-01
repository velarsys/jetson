from robot import Robot
import time

robot = Robot();

# Move forward for 5 secs
robot.forward()
time.sleep(5)
robot.right()
time.sleep(5)
robot.reverse()
time.sleep(5)
robot.left()
time.sleep(5)
robot.stop()

