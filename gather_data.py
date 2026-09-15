#!/usr/bin/env python3

from base_functions import create_auth_session, close_session
from load_environment import load_environment
from parsing_functions import  parse_interface_data, parse_system_data
from custom_functions import get_interface_data, get_system_data
from sql_functions import(
                    create_system_data_insert_statement,
                    create_interface_insert_statements,
                    send_inserts,
                    send_insert
                    )

def main():
    SWITCH_IP, SWITCH_USER, SWITCH_PASS = load_environment()
    try:
        session = create_auth_session(SWITCH_IP, SWITCH_USER, SWITCH_PASS)

        interface_data = get_interface_data(session, SWITCH_IP)
        int_stats_list = parse_interface_data(interface_data)
        interface_insert_statements = create_interface_insert_statements(int_stats_list)
        send_inserts(interface_insert_statements)

        system_data = get_system_data(session, SWITCH_IP)
        parsed_system_data = parse_system_data(system_data)

        system_data_insert_statement = create_system_data_insert_statement(parsed_system_data)
        send_insert(system_data_insert_statement)

    finally:
        close_session(session, SWITCH_IP)

if __name__ == "__main__":
    main()
