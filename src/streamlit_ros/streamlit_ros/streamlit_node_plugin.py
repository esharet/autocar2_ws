

from rclpy.node import Node
from streamlit_ros import streamlit_data 
from streamlit_ros.abstract_streamlit_plugin import AbstractStreamlitPlugin

class StreamlitNodePlugin(AbstractStreamlitPlugin):

    def __init__(self, main_streamlit_node: Node, plugin_name: str): 
        self.__streamlit_node = main_streamlit_node
        self.plugin_name = plugin_name
    
    @property
    def main_node(self,):
        return self.__streamlit_node
    
    @property
    def st_data(self,) -> streamlit_data.StreamlitData:
        return self.main_node.get_streamlit_data()
