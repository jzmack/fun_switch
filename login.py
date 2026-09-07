import requests
import urllib3

def login(ip_address:str, username: str, password:str) -> str:

    # the 6100 uses a self-signed cert so it will throw SSL warnings    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # URL can change based on what version - this is v10.13
    # URL contains username and password which I don't like
    # Need to work on sending form data to not include in URL
    login_url = f"https://{ip_address}/rest/v10.13/login?username={username}&password={password}"

    
    headers = {
        "accept": "*/*",
        "x-use-csrf-token": "true"
    }

    response = requests.post(login_url,headers=headers, verify=False)

    # print(f"HTTP STATUS CODE: {response.status_code}")
    # print(f"RESPONSE BODY: {response.text}")
    # print(f"RESPONSE HEADERS:{response.headers}")

    return response.headers["X-Csrf-Token"]
