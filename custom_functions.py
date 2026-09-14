import requests
from base_functions import get_data

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
    return interface_data

def get_system_info(session:requests.Session, switch_ip:str) -> dict:
    system_info_endpoint = "/system"

    params = {
        "attributes": "boot_time,hostname,software_version",
        "depth":2
    }
    headers= {
        "accept":"application/json"
    }

    system_info_data = get_data(session, switch_ip, system_info_endpoint, headers=headers, params=params)
    return system_info_data
