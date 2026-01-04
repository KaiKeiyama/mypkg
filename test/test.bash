#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

source /opt/ros/jazzy/setup.bash

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

grep -q 'Morse: ... --- ...' /tmp/mypkg.log
res=$?

if [ $res -ne 0 ]; then
    cat /tmp/mypkg.log
fi

rm /tmp/mypkg.log
exit $res
