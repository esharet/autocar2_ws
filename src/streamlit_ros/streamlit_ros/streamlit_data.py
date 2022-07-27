

from enum import IntEnum
from typing import Tuple
import streamlit as st
from streamlit import cli as stcli
from dataclasses import dataclass, field

class LoadSlamMatchType(IntEnum):
    START_AT_FIRST_NODE = 1 
    START_AT_GIVEN_POSE = 2 
    LOCALIZE = 3 

@dataclass
class SlamData():
    slam_graph_filepath: st.text_input = field(default="")
    position_x: st.number_input = field(default=0.0)
    position_y: st.number_input = field(default=0.0)
    position_theta: st.number_input = field(default=0.0)
    match_type: st.number_input = field(default=1)


@dataclass
class NumberData():
    num: int = field(default=0)
    delta: int = field(default=0)


class StreamlitData():
    def __init__(self) -> None:
        self.slam_data = SlamData()
        self.num_data = NumberData()

    def update_num(self, new_num):
        self.num_data.delta = new_num - self.num_data.num
        self.num_data.num = new_num

    def get_data(self,):
        return self.num_data.num, self.num_data.delta

    def get_slam_reload_params(self,) -> Tuple[str, float, float, float, int]:
        return self.slam_data.slam_graph_filepath, self.slam_data.position_x, self.slam_data.position_y, self.slam_data.position_theta, self.slam_data.match_type


def create_streamlit_data():
    if "st_data" in st.session_state:
        return
    st.session_state["st_data"] = StreamlitData()


def get_streamlit_data() -> StreamlitData:
    return st.session_state.get("st_data")
