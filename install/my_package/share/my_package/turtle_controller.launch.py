from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    turtle_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )
    
    turtle_controller = Node(
        package="my_package",
        executable="turtlesim_controller"
    )
    
    
    ld.add_action(turtle_node)
    ld.add_action(turtle_controller)
    return ld
