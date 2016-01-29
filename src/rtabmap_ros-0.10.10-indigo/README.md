rtabmap_ros
===========

RTAB-Map's ROS package.

For more information, demos and tutorials about this package, visit the [rtabmap_ros](http://wiki.ros.org/rtabmap_ros) page on the ROS wiki.

For the RTAB-Map libraries and standalone application, visit the [RTAB-Map's home page](http://introlab.github.io/rtabmap) or the [RTAB-Map's wiki](https://github.com/introlab/rtabmap/wiki).

## Installation 

### ROS distribution 
RTAB-Map is released as binaries in the ROS distribution.
 * Jade
  ```
$ sudo apt-get install ros-jade-rtabmap-ros
```
 * Indigo
  ```
$ sudo apt-get install ros-indigo-rtabmap-ros
```
 * Hydro
  ```
$ sudo apt-get install ros-hydro-rtabmap-ros
```

### Build from source
This section shows how to install RTAB-Map ros-pkg on **ROS Hydro/Indigo/Jade** (Catkin build). RTAB-Map works only with the PCL 1.7, which is the default version installed with ROS Hydro/Indigo/Jade (**Fuerte and Groovy are not supported**).

 * The next instructions assume that you have set up your ROS workspace using this [tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace). I will use indigo prefix for convenience, but it should work with hydro and jade. The workspace path is `~/catkin_ws` and your `~/.bashrc` contains:
 
  ```bash
source /opt/ros/indigo/setup.bash
source ~/catkin_ws/devel/setup.bash
```

 0. Optional dependencies
  * If you want SURF/SIFT on Indigo/Jade (Hydro has already SIFT/SURF), you have to build [OpenCV]([OpenCV](http://opencv.org/)) from source to have access to *nonfree* module. Install it in `/usr/local` (default) and the rtabmap library should link with it instead of the one installed in ROS. I recommend to use latest 2.4 version ([2.4.11](https://github.com/Itseez/opencv/archive/2.4.11.zip)) and build it from source following these [instructions](http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html#building-opencv-from-source-using-cmake-using-the-command-line). RTAB-Map can build with OpenCV3+[xfeatures2d](https://github.com/Itseez/opencv_contrib/tree/master/modules/xfeatures2d) module, but rtabmap_ros package will have libraries conflict as cv-bridge is depending on OpenCV2. If you want OpenCV3, you should build ros [vision-opencv](https://github.com/ros-perception/vision_opencv) package yourself (and all ros packages depending on it) so it can link on OpenCV3.
  
  * ROS (Qt, PCL, dc1394, OpenNI, OpenNI2, Freenect, g2o, Costmap2d, Rviz, Octomap, CvBridge). Note that I've found that [latest g2o version](https://github.com/RainerKuemmerle/g2o) built from source is faster.
    ```bash
$ sudo apt-get install libqt4-dev libpcl-1.7-all-dev libdc1394-dev ros-indigo-openni-launch ros-indigo-openni2-launch ros-indigo-freenect-launch ros-indigo-costmap-2d ros-indigo-octomap-ros ros-indigo-g2o ros-indigo-rviz ros-indigo-cv-bridge
```

  * [GTSAM](https://collab.cc.gatech.edu/borg/gtsam): Follow installation instructions from [here](https://collab.cc.gatech.edu/borg/gtsam/#quickstart). RTAB-Map needs latest version from source (`git clone https://bitbucket.org/gtborg/gtsam.git`), it will not build with 3.2.1.
  
  * [cvsba](http://www.uco.es/investiga/grupos/ava/node/39): Follow installation instructions from [here](http://www.uco.es/investiga/grupos/ava/node/39). Their installation is not standard CMake, you need these extra steps so RTAB-Map can find it:
    ```bash
$ mkdir /usr/local/lib/cmake/cvsba 
$ mv /usr/local/lib/cmake/Findcvsba.cmake /usr/local/lib/cmake/cvsba/cvsbaConfig.cmake
```

  * [Freenect2](https://github.com/OpenKinect/libfreenect2): Follow installation instructions from [here](https://github.com/OpenKinect/libfreenect2#debianubuntu-1404-perhaps-earlier).

 1. Install the RTAB-Map standalone libraries (**don't checkout in the Catkin workspace** but install in your Catkin's devel folder).
 
 ```bash
$ cd ~
$ git clone https://github.com/introlab/rtabmap.git rtabmap
$ cd rtabmap/build
$ cmake -DCMAKE_INSTALL_PREFIX=~/catkin_ws/devel ..  [<---double dots included]
$ make -j4
$ make install
```

 2. Install the RTAB-Map ros-pkg in your src folder of your Catkin workspace.
 
 ```bash
$ cd ~/catkin_ws
$ git clone https://github.com/introlab/rtabmap_ros.git src/rtabmap_ros
$ catkin_make
```

#### Update to new version 

```bash
$ cd rtabmap
$ git pull origin master
$ cd build
$ make
$ make install

$ roscd rtabmap_ros
$ git pull origin master
$ cd ~/catkin_ws
$ catkin_make
```


