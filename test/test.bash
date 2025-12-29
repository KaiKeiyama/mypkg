#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source /opt/ros/humble/setup.bash
source $dir/ros2_ws/install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Count:1' | grep 'Number:2'

echo "ALL TESTS PASSED"
exit 0
