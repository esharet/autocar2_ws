from rclpy.node import Node 
from streamlit_ros import streamlit_data
from abc import ABC, abstractmethod
class AbstractStreamlitPlugin(ABC):

    @abstractmethod
    def __init__(self, main_streamlit_node: Node, plugin_name: str, *args, **kwargs): 
        pass 
    
    @abstractmethod
    def main_node(self,) -> Node:
        pass 
    

    @abstractmethod
    def st_data(self,) -> streamlit_data.StreamlitData:
        pass 