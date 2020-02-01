# compVisualPose

Repository URL: https://github.com/Fugashu/compVisualPose

This repository contains code and information for the following paper (status: under investigation):
F. Spiess, J. Friesslich, T. Kaupp, Samuel Kounev and N. Strobel:  Comparing Augmented RGB-D Indoor Robot Navigation Methods
Using Fusion with Wheel Odometry and IMU Data - an Experimental Comparison under ROS


## Provided datasets:
The provided datasets (rosbags) can be downloaded here: 

[Scenario_1](https://drive.google.com/file/d/1rGULY7jUo4vwWlKkciZCH1vCYOC18itR/view)

[Scenario_2](https://drive.google.com/file/d/1rGULY7jUo4vwWlKkciZCH1vCYOC18itR/view)

## Transform broadcaster:
In order to reconstruct our test environment and results, the required transforms have to be published.
This can be achieved with the broadcast python file provided by us.
Leave it running as a background process.

It can be downloaded here:

[broad.py](https://github.com/Fugashu/compVisualPose/blob/master/broad.py)
