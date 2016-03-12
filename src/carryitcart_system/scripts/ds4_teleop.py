#!/usr/bin/env python
# Converts ps3 input from ROS joy into twist msgs
import rospy
import sensor_msgs.msg as sensor_msgs
import geometry_msgs.msg as geometry_msgs

## use these accelerations to drive the control state to the input, sudden changes in control signal is bad
_lin_accl = 0.02
_ang_accl = 0.1

## scales applied to controller input
_lin_scale = 0.2
_ang_scale = 1.0

#(linear_speed, angular_speed, braking_percentage)
_input_state = (0.0, 0.0, 0.0)

#(linear_speed, angular_speed)
_control_state = (0.0, 0.0)

_dir_x_press = 0
_dir_y_press = 0

def shift_value(cur_val, tgt_val, shift):
	err = cur_val - tgt_val
	if err > 0:
		err = max(err - shift, 0)
	else:
		err = min(err + shift, 0)
	return err + tgt_val

def get_next_control_state(ctrl_state, input_state):
	target_lin, target_ang, braking = input_state
	lin, ang = ctrl_state

	#drive the control terms to their targets
	lin = shift_value(lin, target_lin, _lin_accl)
	ang = shift_value(ang, target_ang, _ang_accl)

	#apply braking
	lin = shift_value(lin, 0, lin*braking)
	ang = shift_value(ang, 0, ang*braking)

	return (lin, ang)

def handle_controller_input(controller_input):
	global _input_state, _lin_scale, _ang_scale, _dir_x_press, _dir_y_press

	## PS3
	lstick_x, lstick_y, rstick_x, ltrigger, rtrigger, rstick_y, dir_x, dir_y = controller_input.axes[:8]
	sqr, ex, crcl, tri, lshoulder, rshoulder = controller_input.buttons[:6]

	#adjust scales
	if dir_y:
		if not _dir_y_press:
			_lin_scale += dir_y*_lin_scale*0.1
			_dir_y_press = True
	else:
		_dir_y_press = False

	if dir_x:
		if not _dir_x_press:
			_ang_scale += dir_x*_ang_scale*0.1
			_dir_x_press = True
	else:
		_dir_x_press = False

	#reset scales
	if ex: _lin_scale = 0.2
	if crcl: _ang_scale = 1.0

	turn_input = +(lstick_x + rstick_x) #positive since left stick is positive on the ds4 and ROS uses RHR
	fwd_input = (lstick_y + rstick_y)
	braking_input = max(1.0 - ltrigger, 1.0 - rtrigger)/2.0

	_input_state = (fwd_input*_lin_scale, turn_input*_ang_scale, braking_input)


def publish_control(publisher, control_state):
	linear_speed, angular_speed = control_state

	twist = Twist()
	twist.linear.x, twist.linear.y, twist.linear.z = (linear_speed, 0, 0)
	twist.angular.x, twist.angular.y, twist.angular.z = (0, 0, angular_speed)
	twist_pub.publish(twist)

if __name__ == '__main__':
	rospy.init_node('ds4_teleop')
	
	rospy.Subscriber("joy", sensor_msgs.Joy, handle_controller_input)
	twist_pub = rospy.Publisher('~cmd_vel', geometry_msgs.Twist, queue_size=5)

	update_rate = 10 #Hz
	loop_rate = rospy.Rate(update_rate) 

	try:
		while not rospy.is_shutdown():
			loop_rate.sleep()

			_control_state = get_next_control_state(_control_state, _input_state)

			publish_control(twist_pub, _control_state)
	except e:
		print e
	finally:
		#if something goes wrong, try to make sure the turtlebot comes to a halt
		publish_control(twist_pub, (0, 0))

