#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

# ros2 run your_package_name your_node_name --ros-args -p topic_name:=your_desired_topic


class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')

        self.declare_parameter("camera_topic", value="webcam/image_raw")

        camera_topic = self.get_parameter("camera_topic").get_parameter_value().string_value


        self.publisher_ = self.create_publisher(Image, camera_topic, 10)
        self.timer = self.create_timer(0.08, self.timer_callback) # callback timer faz bottleneck das fps 0.05 = 20 fps 0.1 = 10 fps
        self.cap = cv2.VideoCapture(0)  # Use default webcam
        self.bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Unable to read from webcam.")
            return

        image_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.publisher_.publish(image_msg)

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()

def main(args=None):
    rclpy.init(args=args)
    node = WebcamPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
