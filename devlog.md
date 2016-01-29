THIS IS NOT A CHANGELOG. This log is to record stuff not captured by the code.

### Earlier
- Setup system to use bag files
- After puzzling over why nodes were not subscribing to image topics, discovered ROS image_transport.

### 28/1/2016
- While running with turtlebot data for the first time, ran into [this issue](http://answers.ros.org/question/221550/problem-running-rtabmap_ros-against-a-bag-file/). Compiling rtabmap_ros from source in order to implement the fix linked to in the issue report.
- Compiled rtabmap 10.10 seems to *start* like before, now to patch in fix.
-And the issue is fixed! rtabmap_ros no longer crashes upon recieving turtlebot data.
- Created git repo, initial commit to source control.

### 29/1/2016
- Compiling OpenCV 2.4.11 to see if RTAB peforms better with SURF or SIFT.
- Need to figure out why RTAB can't detect g2o.