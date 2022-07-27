
from enum import IntEnum
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose2D
from slam_toolbox.srv import SerializePoseGraph, DeserializePoseGraph 
from streamlit_ros.streamlit_node_plugin import StreamlitNodePlugin
from streamlit_ros.streamlit_data import LoadSlamMatchType


class SlamReviverPlugin(StreamlitNodePlugin): 
    def __init__(self,main_node: Node, plugin_name: str): 
        super().__init__(main_node, plugin_name)

        self.main_node.declare_parameters(
            namespace='', 
            parameters=[
                ('slam_map_location', rclpy.Parameter.Type.STRING),
            ]
        )
        self.load_slam_client = self.main_node.create_client(DeserializePoseGraph, "/slam_toolbox/deserialize_map", )
        self.load_slam_req = DeserializePoseGraph.Request()
    
    def load_slam(self, slam_map_location: str , position_x:float, position_y: float, theta: float, request_type: int) -> rclpy.Future: 
        print(f"trying to load slam map: {slam_map_location}")
        self.load_slam_req.filename = slam_map_location
        self.load_slam_req.match_type = request_type
        self.load_slam_req.initial_pose = Pose2D()
        self.load_slam_req.initial_pose.x = float(position_x)
        self.load_slam_req.initial_pose.y = float(position_y)
        self.load_slam_req.initial_pose.theta = float(theta) 
        result_future = self.load_slam_client.call_async(self.load_slam_req)
        return result_future