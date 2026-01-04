#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 KaiKeiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.sub = self.create_subscription(String, 'chatter', self.cb, 10)
        
        self.morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', '0': '-----', 'SOS': '... --- ...'
        }

    def cb(self, msg):
        input_text = msg.data.upper()
        output_text = ""
        
        for char in input_text:
            if char in self.morse_code:
                output_text += self.morse_code[char] + " "
            else:
                output_text += "? "
        
        self.get_logger().info(f"Received: {input_text} -> Morse: {output_text}")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
