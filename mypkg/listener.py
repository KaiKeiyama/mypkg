#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PrimeListener(Node):
    def __init__(self):
        super().__init__('prime_listener')
        self.subscription = self.create_subscription(
            Int32,
            'prime',
            self.listener_callback,
            10)

    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def get_prime_index(self, target_num):
        count = 0
        for i in range(2, target_num + 1):
            if self.is_prime(i):
                count += 1
        return count

    def listener_callback(self, msg):
        val = msg.data
        index = self.get_prime_index(val)
        self.get_logger().info(f'Count:{index} | Number:{val}')

def main(args=None):
    rclpy.init(args=args)
    node = PrimeListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
