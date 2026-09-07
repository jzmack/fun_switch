#!/usr/bin/env python3

from login import login
from load_environment import load_environment

def main():
    API_IP, SWITCH_USER, SWITCH_PASS = load_environment()
    token = login(API_IP, SWITCH_USER, SWITCH_PASS)

if __name__ == "__main__":
    main()