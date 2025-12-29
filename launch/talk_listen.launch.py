# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='prime_number_generator',
            executable='prime_talker',
            name='talker_node'
        ),
        Node(
            package='prime_number_generator',
            executable='prime_listener',
            name='listener_node',
            output='screen'
        ),
    ])
