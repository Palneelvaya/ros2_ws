import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
	urdf_file = '/home/palneel/ros2_ws/src/roboarm/urdf/manipulator.urdf'

	return LaunchDescription(
		[
			ExecuteProcess(
				cmd=["gazebo","-s","libgazebo_ros_factory.so",],
				output="screen",
			),
			Node(
				package="gazebo_ros",
				executable="spawn_entity.py",
				arguments=["-entity","roboarm","-b","-file", urdf_file],
			),
			Node(
				package="robot_state_publisher",
				executable="robot_state_publisher",
				output="screen",
				arguments=[urdf_file],
			),
		])
