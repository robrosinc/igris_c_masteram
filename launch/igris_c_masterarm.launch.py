#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    node = Node(
        package="igris_c_masterarm",
        executable="igris_c_masterarm_node",
        name="igris_c_masterarm_node",
        output="screen",
        parameters=[{
            'port': LaunchConfiguration('port'),
            'baud': ParameterValue(LaunchConfiguration('baud'), value_type=int),
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument('port', default_value='/dev/igrisb_masterarm'),
        DeclareLaunchArgument('baud', default_value='1000000'),
        node,
    ])
