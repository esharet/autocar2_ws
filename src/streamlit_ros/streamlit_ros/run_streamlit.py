from queue import Queue
import time
import sys
import streamlit as st
from streamlit import cli as stcli
import numpy

numpy.random.BitGenerator = numpy.random.bit_generator.BitGenerator
from streamlit_ros import streamlit_node as st_node
from streamlit_ros import streamlit_data as st_data
from streamlit_ros.streamlit_data import LoadSlamMatchType 

 
st_data.create_streamlit_data()
st_node.run_rclpy_once()
st_node.get_ros_node().add_streamlit_data_object(st_data.get_streamlit_data())


def reload_slam_cb():
    ros_node = st_node.get_ros_node()
    slam_filepath, x, y, theta, match_type = st_data.get_streamlit_data().get_slam_reload_params()
    ros_node.load_slam(slam_filepath, x, y, theta, match_type)
    # print(f"sending over /my_string : '{slam_filepath}'")

def match_type_radio_name(radio_option: int):
    for match_type in LoadSlamMatchType: 
        if match_type.value == radio_option: 
            return match_type.name
    return "Unknown option"

def main():
    st.title('Streamlit ROS2 APP:')
    st.subheader('Slam Reviver')
    st_data.get_streamlit_data().slam_data.slam_graph_filepath = st.text_input('enter slam graph filepath:', '/home/ros/dev_ws/src/dorothy_robot/maps/slam/slam_inhouse_3')
    x_col, y_col, theta_col, match_type_col = st.columns(4)
    with x_col: 
        st_data.get_streamlit_data().slam_data.position_x = st.number_input(label="x position", key="x_pos" )
    with y_col: 
        st_data.get_streamlit_data().slam_data.position_y = st.number_input(label="y position", key="y_pos")
    with theta_col: 
        st_data.get_streamlit_data().slam_data.position_theta = st.number_input(label="theta", key="theta")
    with match_type_col: 
        st_data.get_streamlit_data().slam_data.match_type = st.radio(label="match type", key="match type", options=(0,1,2,3), format_func=match_type_radio_name)

    if st.button('reload slam'): 
        reload_slam_cb()
    metrics = st.empty()
        
    finished = False
    while not finished:
        mynum, mydelta = st_data.get_streamlit_data().get_data()

        with metrics:
            st.metric(label="Get Int32 Number from ROS", value=mynum,
                      delta=mydelta, delta_color="inverse")
        
        

        time.sleep(0.1)
    
    st_node.shutdown()




if __name__ == '__main__':
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
