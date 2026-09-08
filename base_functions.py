import requests
import urllib3
import json

def login(ip_address:str, username: str, password:str) -> str:

    # the 6100 uses a self-signed cert so it will throw SSL warnings    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # URL can change based on what version - this is v10.13
    login_url = f"https://{ip_address}/rest/v10.13/login?username={username}&password={password}"

    
    headers = {
        "accept": "*/*",
        "x-use-csrf-token": "true"
    }

    response = requests.post(login_url,headers=headers, verify=False)

    print(f"HTTP STATUS CODE: {response.status_code}")
    print(f"RESPONSE BODY: {response.text}")
    print(f"RESPONSE HEADERS:{response.headers}")
    print(response.headers["X-Csrf-Token"])
    return response.headers["X-Csrf-Token"]

def logout(ip_address:str, token:str):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    logout_url = f"https://{ip_address}/rest/v10.13/logout"

    print(token)
    headers = {
        "Accept": "*/*",
        "X-CSRF-Token": token
    }
    response = requests.post(logout_url, headers=headers, verify=False)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        print(response.headers)
    else:
        print("Logged out.")

def create_auth_session(switch_ip:str, username:str, password:str) -> requests.Session:
    """This function returns an authenicated session with the AOS-CX switch using version 10.13."""
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    session = requests.Session()
    login_data = {
        "username": username,
        "password": password 
    }
    login_response = session.post(f"https://{switch_ip}/rest/v10.13/login",data=login_data, verify=False)

    if login_response.status_code != 200:
        login_response.raise_for_status()
        return

    print(f"Successfully logged into {switch_ip} as {username}.")    
    return session

def get_data(session: requests.Session,
             switch_ip:str,
             endpoint:str,
             params=None,
             headers=None,
             payload=None) -> dict:

    """Used for HTTP GET requests."""

    response = session.get(f"https://{switch_ip}/rest/v10.13{endpoint}",
                           params=params,
                           headers=headers,
                           json=payload,
                           verify=False)
    if response.status_code != 200:
        response.raise_for_status()
        return
    json_data = json.loads(response.text)    
    return json_data

def close_session(session:requests.Session, switch_ip:str):
    logout_response = session.post(f"https://{switch_ip}/rest/v10.13/logout", verify=False)

    if logout_response.status_code !=200:
        logout_response.raise_for_status()
    
    session.close()
    print("Logged out!")