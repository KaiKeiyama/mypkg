#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source /opt/ros/jazzy/setup.bash
source $dir/ros2_ws/install/setup.bash

timeout 20 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Count:8 | Number:19'
