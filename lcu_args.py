import sys
import requests
import json
from time import sleep
import platform
import base64
import regex as re 
import os
from lcu_driver import Connector
import subprocess
import warnings
import platform 
import tempfile 

# Get region and port and token information from user command line output 
def get_port_and_token():
    # Get the user's operating system
    operating_system = platform.system()
    # Create terminal command depending on system to get app port and auth
    if operating_system == "Windows":
        command = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline"
    elif operating_system == "Linux":
        command = "wmic PROCESS WHERE name='LeagueClientUx.exe' GET commandline"
    elif operating_system == "Darwin":
        command = "ps -A | grep LeagueClientUx"
    else:
        print("User's operating system could not be identified.")

    output = subprocess.check_output(command, shell=True)
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(output.decode())
        temp_file_path = temp_file.name
        # Use regex to extract tokens and ports 
        with open(temp_file_path, 'r') as file:
            content = file.read()
            match = re.search(r'--app-port=([0-9]*)', content)
            if match:
                app_port=match.group(1)
            else:
                print('app port not found')
            match = re.search(r'--remoting-auth-token=([\w-]*)', content)
            if match:
                remoting_token= match.group(1)
            else:
                print('token not found')
            match = re.search(r'--riotclient-app-port=([0-9]*)', content)
            if match:
                riot_app_port= match.group(1)
            else:
                print("riot app port not found")
            match = re.search(r'--riotclient-auth-token=([\w-]*)', content)
            if match:
                riot_auth_token= match.group(1)
            else:
                print("riot auth token not found")
    return (app_port,remoting_token,riot_app_port,riot_auth_token)

# Access LoL config file to get user region         
def get_lol_region():
    config_file_path = ""
    if os.name == 'posix':  # Unix-like systems (Linux, macOS)
        config_dir = os.path.expanduser('~/Library/Application Support/Riot Games/League of Legends/Config')
    elif os.name == 'nt':  # Windows
        config_dir = os.path.expandvars('%APPDATA%/Riot Games/Riot Client/Config')
    if os.path.isdir(config_dir):
        for file_name in os.listdir(config_dir):
            if file_name.endswith('.yaml'):
                config = os.path.join(config_dir, file_name)
                with open(config, 'r') as config_file:
                    for line in config_file:
                        if 'chat:' in line:
                            region = line.split('"')[1]
                            return region
    print("region not found")
    return None



