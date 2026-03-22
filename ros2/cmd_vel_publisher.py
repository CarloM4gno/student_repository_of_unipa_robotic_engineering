import rclpy
import json
from rclpy.node import Node
from std_msgs.msg import String
import random

class vel_pub(Node):
    def __init__(self):
        # vel_pub.. è il nome del nodo ros
        super().__init__('cmd_vel_publisher')
        self.publisher = self.create_publisher(String,'/cmd_vel',10)
        self.timer = self.create_timer(1,self.time_callback)
        self.counter = 0
    
    def time_callback(self):
        # crea numeri random tra 2 valori 
        random_vel_x = random.uniform(0.45, 1.75)
        random_vel_z = random.uniform(-1.0, 1.0)

        # crea un dizionario con velocità x,y,z e distanza tra le ruote e raggio ruote in m
        robot_data = {"vel_x": random_vel_x , "vel_y" : 0.0 , "vel_z" : random_vel_z, "l" : 0.5 , "r" : 0.07

        }
        # converte in stringa il dizionario
        val_string = json.dumps(robot_data)
        # crea un messaggio ros di tipo stringa
        msg = String()
        
        msg.data = val_string

        self.publisher.publish(msg)
        self.get_logger().info("message published" + msg.data)

def main():
    rclpy.init()
    publisher = vel_pub()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

# esegui main() SOLO se questo file viene eseguito direttamente, non vale come libreria
if __name__ == '__main__':
    main()