# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    message_arg = launch.actions.DeclareLaunchArgument(
        'message',
        default_value='SOS',
        description='Message to transmit in Morse code'
    )

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        parameters=[{'message': launch.substitutions.LaunchConfiguration('message')}]
    )

    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
    )

    return launch.LaunchDescription([
        message_arg,
        talker,
        listener,
    ])
