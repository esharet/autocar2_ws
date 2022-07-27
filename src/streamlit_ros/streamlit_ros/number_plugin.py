
from std_msgs.msg import String, Int32
import rclpy
from rclpy.node import Node
from streamlit_ros.streamlit_node_plugin import StreamlitNodePlugin

class NumberPlugin(StreamlitNodePlugin): 
    def __init__(self,main_node: Node, plugin_name: str): 
        super().__init__(main_node, plugin_name)
        self.num_sub = self.main_node.create_subscription(
            Int32, '/my_number', self.my_number_cb, qos_profile=10)

    def my_number_cb(self, num: Int32): 
        self.st_data.update_num(num.data)