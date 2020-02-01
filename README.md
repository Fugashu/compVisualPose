# compVisualPose

Repository URL: https://github.com/Fugashu/compVisualPose

This repository contains code and information for the following paper (status: under investigation):

F. Spiess, J. Friesslich, T. Kaupp, Samuel Kounev and N. Strobel:  

Comparing Augmented RGB-D Indoor Robot Navigation Methods using Fusion with Wheel Odometry and IMU Data - an Experimental Comparison under ROS


## Provided Datasets:
The provided datasets (rosbags) can be downloaded here: 

[Scenario_1](https://drive.google.com/file/d/1rGULY7jUo4vwWlKkciZCH1vCYOC18itR/view)

[Scenario_2](https://drive.google.com/file/d/1Q31JPV9viq17bAQzqfBfMXwp7hS-mH6q/view)

## Transform Broadcaster:
In order to reconstruct our test environment and results, the required transforms have to be published.
This can be achieved with the broadcast python file provided by us.
Leave it running as a background process.

It can be downloaded here:

[broad.py](https://github.com/Fugashu/compVisualPose/blob/master/broad.py)

## Tuned Parameters

We tuned the parameters for the evaluated VO and V-SLAM algorithms for our environment and composed them in an [overview PDF](https://github.com/Fugashu/compVisualPose/blob/master/ParameterOverview.pdf).
