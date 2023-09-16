#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Float64

class MyNode(Node): 
    def __init__(self):
        super().__init__('Node1')
        self.score_ = 0.0
        self.pub_ = self.create_publisher(String, "Text", 10)
        self.timer_ = self.create_timer(0.1, self.publish_text) 
        self.create_subscription(Float64, "score", self.score_callback, 10)

    def publish_text(self):
        msg = String()
        msg.data = str(self.score_)
        self.pub_.publish(msg)

    def score_callback(self, msg: Float64):
        self.get_logger().info(str(msg.data))
        self.score_ = msg.data


def main(args=None):
    rclpy.init(args=args)
    node = MyNode() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()