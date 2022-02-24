#!/usr/bin/python3
# This is simple refactor of detectnet.py for checking distance and making the robot move
# https://github.com/dusty-nv/jetson-inference/blob/master/docs/depthnet.md

import jetson.inference
import jetson.utils
import numpy as np
from robot import Robot
import time

robot=Robot();
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# /dev/video0 is the name of the USB camera if you list cameras
camera = jetson.utils.videoSource("/dev/video0")  # '/dev/video0' for V4L2
# load mono depth network
net = jetson.inference.depthNet()

# depthNet re-uses the same memory for the depth field,
# so you only need to do this once (not every frame)
depth_field = net.GetDepthField()

# cudaToNumpy() will map the depth field cudaImage to numpy
# this mapping is persistent, so you only need to do it once
depth_numpy = jetson.utils.cudaToNumpy(depth_field)

print(f"depth field resolution is {depth_field.width}x{depth_field.height}, format={depth_field.format}")

while True:
    img = camera.Capture()  # assumes you have created an input videoSource stream
    net.Process(img)
    jetson.utils.cudaDeviceSynchronize()  # wait for GPU to finish processing, so we can use the results on CPU

    # find the min/max values with numpy
    min_depth = np.amin(depth_numpy)
    max_depth = np.amax(depth_numpy)
    # min_depth is a float 32
    print("min_depth is "+str(min_depth))
    print("max_depth is "+str(max_depth))
    # When hand is moved in front, the max_depth increases
    if(max_depth<2):
        robot.right()
        time.sleep(5)
    else:
        robot.forward()


