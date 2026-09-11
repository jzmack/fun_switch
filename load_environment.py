from dotenv import load_dotenv
import os

def load_environment(path_to_env=".env"):
    load_dotenv()
    API_USERNAME = os.getenv("SWITCH_USER")
    API_PASSWORD = os.getenv("SWITCH_PASSWORD")
    API_IP = os.getenv("SWITCH_IP")
    return API_IP, API_USERNAME, API_PASSWORD
