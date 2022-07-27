from typing import Dict, Type
import threading 
import streamlit as st
from streamlit import cli as stcli

from std_msgs.msg import String, Int32
import rclpy
from rclpy.node import Node
from rclpy import qos

from streamlit_ros.streamlit_data import StreamlitData, LoadSlamMatchType
from streamlit_ros.abstract_streamlit_plugin import AbstractStreamlitPlugin
from streamlit_ros.slam_revive_plugin import SlamReviverPlugin 
from streamlit_ros.number_plugin import NumberPlugin 

class StreamlitNode(Node):
    def __init__(self, ):
        super().__init__('streamlit')
        self._streamlit_data: StreamlitData = None

        self.plugins: Dict[str, AbstractStreamlitPlugin] = dict()

        self.register_plugins()
        
    
    def load_slam(self,filename, position_x: float = 0, position_y: float = 0, theta: float = 0,  mode: LoadSlamMatchType = LoadSlamMatchType.START_AT_GIVEN_POSE):
        plugin: SlamReviverPlugin = self.plugins.get("slam_reviver_plugin")
        plugin.load_slam(filename, position_x, position_y, theta, mode)


    def add_streamlit_data_object(self, st_data): 
        if self._streamlit_data: 
            return  
        self._streamlit_data = st_data
    
    def get_streamlit_data(self): 
        return self._streamlit_data

    def __register_plugin(self,plugin_name: str, node_plugin_cls: Type[AbstractStreamlitPlugin], *args, **kwargs):
        self.plugins[plugin_name] = node_plugin_cls(self, plugin_name, *args, **kwargs) 
    

    def register_plugins(self,): 
        self.__register_plugin("slam_reviver_plugin", SlamReviverPlugin) 
        self.__register_plugin("recieve_number_plugin", NumberPlugin)

@st.cache
def run_rclpy_once():
    if "st_ros_node" in st.session_state: 
        return 
    rclpy.init(args=None)

    # rclpy.spin_once(streamlit_node, timeout_sec=1)
    global streamlit_node
    streamlit_node = StreamlitNode()
    st.session_state["st_ros_node"] = streamlit_node
    rclpy_spin_thread = threading.Thread(
        target=rclpy.spin, args=(streamlit_node,), daemon=True)
    rclpy_spin_thread.start()


def get_ros_node() -> StreamlitNode:
    return st.session_state.get("st_ros_node")

def shutdown():
    rclpy.shutdown()