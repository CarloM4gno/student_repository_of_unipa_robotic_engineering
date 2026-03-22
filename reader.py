import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Reader(Node):
    def __init__(self):
        super().__init__("reader_node_executable")
        # questo terzo parametro è la funzione da chiamare se legge messaggio
        self.create_subscription(String,'/chatter',self.read_message,10)
   
    # perchè passa msg? -> perchè non ha il messaggio
    def read_message(self,msg):
        self.get_logger().info("message received:" + msg.data)

def main():
    rclpy.init()
    reader_node = Reader()

    rclpy.spin(reader_node)

    reader_node.destroy_node()
    rclpy.shutdown()