
from typing import Dict, Type, Any
import streamlit as st
from streamlit import cli as stcli


class StreamlitControllerPluginBase():
    subclasses: Dict[str, Type[Any]] = dict()

    def __init__(self) -> None:
        pass

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.subclasses[cls.__name__] = cls

    def __create_st_controller_plugin(data_plugin_name: str):
        if f"st_data/{data_plugin_name}" in st.session_state:
            return
        st.session_state[f"st_data/{data_plugin_name}"] = StreamlitControllerPluginBase.subclasses[data_plugin_name]()

    def create_all_controller_plugins(): 
        for plugin_name in StreamlitControllerPluginBase.subclasses.keys():
            StreamlitControllerPluginBase.__create_st_controller_plugin(plugin_name)

    def get_st_controller_plugin(data_plugin_name: str):
        return st.session_state.get(f"st_data/{data_plugin_name}")

class NumberPlugin(StreamlitControllerPluginBase):
    def __init__(self) -> None:
        super().__init__()
        self.mynum = 0
        self.mydelta = 0
    
    def get_data(self, ):
        return self.mynum, self.mydelta
    
    def update_num(self,new_num):
        self.mydelta = new_num - self.mynum
        self.mynum = new_num


class SlamDataPlugin(StreamlitControllerPluginBase):
    def __init__(self,):
        super().__init__()
        self.slam_filepath = ""
        self.initial_position_x = 0
        self.initial_position_y = 0
        self.initial_position_theta = 0



def create_streamlit_data_plugins():
    if "st_plugin_data_manager" in st.session_state:
        return
    st.session_state["st_plugin_data_manager"] = StreamlitControllerPluginBase()
    StreamlitControllerPluginBase.create_all_controller_plugins()


def get_streamlit_plugin_base() -> StreamlitControllerPluginBase:
    return st.session_state.get("st_plugin_data_manager")

def get_streamlit_controller_plugin(plugin_name: str): 
    return StreamlitControllerPluginBase.get_st_controller_plugin(plugin_name)
