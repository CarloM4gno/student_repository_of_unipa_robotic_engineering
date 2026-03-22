import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class vel_detector(Node):

    def __init__(self):
        super().__init__("cmd_vel_subscriber")

        self.subscriber = self.create_subscription(
            String,
            '/cmd_vel',
            self.listener_callback,
            10
        )

    def listener_callback(self,msg):

        dati = json.loads(msg.data)

        v_lineare = dati['vel_x']
        v_angolare = dati['vel_z']
        raggio = dati['r']
        interasse = dati['l']

        self.get_logger().info(
            f"\nLineare: {v_lineare:.2f}, angolare: {v_angolare:.2f}\nparametri:\nraggio {raggio:.2f}, interasse {interasse:.2f}\n"
        )

def main():
    rclpy.init()
    subscriber = vel_detector()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()