#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # turtlesim has the msg type of this geametry_msg/msg/Twist   Twist msg type from 
#geometry_msg package


class DrawCircleNode(Node):
    def __init__(self):  ## constructor
        super().__init__("draw_circle")
        #create publisher to send data to the topic
        self.cmv_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10) #Twist = msg type,  topic name and queue size
        self.timer_ = self.create_timer(0.5,self.send_velocity_command) #publish the data
        self.get_logger().info("Draw Circle node has been started")  

    #we need to send data to turtle in every 0.5 sec so we need to publish data.
    #create timer function to count 0.5s

    def send_velocity_command(self):
        #make the msg according to the command. going to x anxis and angularly
        #timel will call this function in every 0.5 sec and make the msg
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0  #draw a circle to the x direction start
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    kkjjo