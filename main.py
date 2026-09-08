#!/usr/bin/env python3

from base_functions import create_auth_session, get_data, close_session
from load_environment import load_environment
from parsing_functions import parse_current_firmware, parse_interface_data
from custom_functions import get_interface_data
from sql_functions import create_insert_statements

def main():
    SWITCH_IP, SWITCH_USER, SWITCH_PASS = load_environment()
    try:
        session = create_auth_session(SWITCH_IP, SWITCH_USER, SWITCH_PASS)

        firmware_data = get_data(session, SWITCH_IP, "/firmware")
        current_firmware = parse_current_firmware(firmware_data)
        print(current_firmware)

        interface_data = get_interface_data(session, SWITCH_IP)
        int_stats_list = parse_interface_data(interface_data)
        create_insert_statements(int_stats_list)

    finally:
        close_session(session, SWITCH_IP)

if __name__ == "__main__":
    main()