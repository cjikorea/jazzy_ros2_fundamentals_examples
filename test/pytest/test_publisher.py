#!/usr/bin/env python3

"""
Test suit for the ROS2 minimal publisher node.

This script contains unit for verifying the functionality of a minimal ROS 2 publisher.
It thests the node creation, message counter increment, and message content formatting.

Subcription Topics:
    None


"""

import pytest
import rclpy
from std_msgs.msg import String
from ros2_fundamentals_examples.py_minimal_publisher import MinimalPyPublisher


def test_publisher_creation():
    """
     Test if the publisher node is created correctly.

     This test verifies:
     1. The node name is set correctly.
     2. The bublisher objest exists,
     3, The topic name is correct,
    """

    rclpy.init()

    try:
        # Create an instance of our publisher node

        node = MinimalPyPublisher()

        # Test 1: Verify the node has the expected name

        assert node.get_name() == "minimal_py_publisher"

        assert hasattr(node, 'publisher_1')
        assert node.publisher_1.topic_name == '/py_example_topic'

    finally:
        # Clean up ROS 2 communication

        rclpy.shutdown()

def test_mesage_counter():
    """
    Test if the message counter increaments correctly
    """

    rclpy.init()

    try:
        node = MinimalPyPublisher()
        initial_counter = node.i
        node.timer_callback()
        assert node.i == initial_counter + 1

    finally:
        rclpy.shutdown()

def test_message_content():
    
    """
        
    """
    rclpy.init()
    
    try:
        node = MinimalPyPublisher()

        node.i  = 5
        msg = String()

        msg.data = f'Hello World : {node.i}'
        assert msg.data == 'Hello World : 5'

    finally:
        rclpy.shutdown()
        

if __name__ == '__main__':
     pytest.main(['-V-'])


         
        