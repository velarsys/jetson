# jetson
Jetson AI

This is a simple extension of Jetson Inference for an Auto Bot

Reference: https://github.com/dusty-nv/jetson-inference/blob/master/docs/depthnet.md

Steps to use the bot
1. Setup the connection between L293D H Bridge and Jetson Nano by referring Jetson-To-HBridge-L293D-PinOut-20220224_154342.jpg 
2. Set up jetson inference as per the above site
3. Copy the files from this repository to the /jetson-inference/python/examples
4. Run the autobot: python3 autobot.py
5. The bot will move forward and when it detects objects, it moves right and then forward again

Video demo: https://www.youtube.com/watch?v=8f6Z1EUiHO4
