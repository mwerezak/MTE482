#!/bin/bash
rosbag record -e \
/tf \
/odom \
/ukf/odom \
/scan \
/camera/depth_registered/camera_info \
/camera/depth_registered/hw_registered/image_rect_raw/compressedDepth.* \
/camera/rgb/camera_info \
/camera/rgb/image_rect_color/compressed.* \
/cmd_vel_mux/input.* \
/zed/camera/rgb/camera_info \
/zed/camera/rgb/image_rect_color/compressed.* \
/zed/camera/depth/camera_info \
/zed/camera/depth_registered/image_raw/compressedDepth.*