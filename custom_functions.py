import requests
from base_functions import get_data
from pprint import pprint

def get_interface_data(session:requests.Session, switch_ip:str) -> dict:
    interface_endpoint = "/system/interfaces"

    params = {
        "attributes":"description,statistics,rate_statistics",
        "depth":2
    }

    headers = {
        "accept":"application/json"
    }

    interface_data = get_data(session, switch_ip, interface_endpoint,headers=headers, params=params)
    pprint(interface_data)
    return interface_data