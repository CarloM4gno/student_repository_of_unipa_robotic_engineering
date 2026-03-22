import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# la classe reader eredita da Node -> diventa un nodo ros
class Writer(Node):
    # creiamo il costruttore
    def __init__(self):
        # chiama il costruttore della classe padre Node, !! e da il nome del nodo (ma non è quello che chiamo, quello è in setup.py)
        super().__init__("writer_node_executable")
        # creiamo degli attributi:
        # l'attribbuto self.publisher non esiste e quindi lo poniamo uguale a uno già esistente
        #in questo modo possiamo fare OGGETTO.publisher nel main
        self.publisher = self.create_publisher(String,'/chatter',10)
        # questo metodo DEL PADRE invece esiste già...
        # ogni x secondi esegui la funzione ( ) -> ogni secondo publichi
        self.create_timer(1,self.write_message)
        # a che serve il counter?
        self.counter = 0

    def write_message(self):
        # particolare struttura dati
        msg = String()
        # aggiunge al messaggio il contatore
        msg.data = "hello world" + str(self.counter)
        self.counter += 1
        # chiamata metodo del padre
        self.publisher.publish(msg)
        # ennesimo medtodo
        self.get_logger().info("pubblicato il messaggio: "+msg.data)

        

def main():
    # avvia ros 2
    rclpy.init()
    # crea oggetto della classe writer()
    writer_node = Writer()

    # come se fosse un while True dove chiamo l oggetto writer_node, che chiama il costruttore
    # dove viene chiamato con self.create_timer def write_message
    rclpy.spin(writer_node)
 
    writer_node.destroy_node()

    # chiude ros 2
    rclpy.shutdown()

    # Nota la funzione  write_massage viene chiamta in loop ogni 1 secondo anche se teoricamente il csotruttore viene esguito solo 1 volta, viene quindi chiamata esternamente