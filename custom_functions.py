import requests
from base_functions import get_data

def get_interface_data(session:requests.Session, switch_ip:str) -> dict:
    interface_endpoint = "/system/interfaces"

    params = {
        "attributes":"description,statistics",
        "depth":2
    }

    interface_data = get_data(session, switch_ip, interface_endpoint, params=params)
    return interface_data