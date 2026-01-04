#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        
        self.declare_parameter('message', 'SOS')
        
        self.create_timer(1.0, self.cb)

    def cb(self):
        msg = String()
        msg.data = self.get_parameter('message').get_parameter_value().string_value
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
