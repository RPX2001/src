#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):   ## inherit class

    def __init__(self):  ## constructor
        super().__init__("first_node")   #initialize node
        #self.get_logger().info("ROS2") ## write a log inside the node
        self.counter_ = 0
        self.create_timer(1.0,self.timer_callback)
    
    #We need to display msg in every second so create timer function -------INSIDE THE NODE-----
    def timer_callback(self):
        self.get_logger().info("Ros-2" + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)  # initialize ros2 communications start
    node = MyNode()
    rclpy.spin(node)  # continue runnig until kill it (ctrl + c)
    rclpy.shutdown()    #shutdown ros2 communications

if __name__ == '__main__':
    main()