#!/bin/bash
rosbag record -e \
/tf \
/odom \
/scan \
/camera/depth_registered/camera_info \
/camera/depth_registered/hw_registered/image_rect_raw/compressedDepth.* \
/camera/rgb/camera_info \
/camera/rgb/image_rect_color/compressed.* \
/cmd_vel_mux/input.* \
