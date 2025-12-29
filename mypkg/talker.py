#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from example_interfaces.srv import AddTwoInts

class PrimeTalker(Node):
    def __init__(self):
        super().__init__('prime_talker')
        self.publisher_ = self.create_publisher(Int32, 'prime', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.current_number = 2
        self.srv = self.create_service(AddTwoInts, 'get_nth_prime', self.get_nth_prime_callback)

    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def timer_callback(self):
        while not self.is_prime(self.current_number):
            self.current_number += 1
        msg = Int32()
        msg.data = self.current_number
        self.publisher_.publish(msg)
        self.current_number += 1

    def get_nth_prime_callback(self, request, response):
        n = request.a
        count, num = 0, 1
        while count < n:
            num += 1
            if self.is_prime(num):
                count += 1
        
        response.sum = num
        self.get_logger().info(f'Count: {n} | Number:{num}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = PrimeTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
