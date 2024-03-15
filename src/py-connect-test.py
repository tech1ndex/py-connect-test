#!/bin/python3

import requests
from datetime import datetime
import time
import warnings
import argparse
import socket
import json

# Parse Arguments
parser = argparse.ArgumentParser(description='A simple HTTP connection tester written in Python.')
parser.add_argument("-u", "--urls", help="A list of URLs to test against", nargs='*')
parser.add_argument("-w", "--webhook-url", help="A URL to send Alerts too", nargs='*')
parser.add_argument("-a", "--alerts", help="Use to enable alerting, disabled by default", action="store_true")
parser.add_argument("-l", "--log", help="Use --log if you want output logged to a file, default is stdout", action="store_true")
parser.add_argument("-p", "--logpath", help="Directory path to store logfile", default="--")
parser.add_argument("--certcheck", help="Use to toggle ssl certificate validation, enabled by default", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

# Logic to handle log parameters
if args.log == True and args.logpath == "--":
    parser.error('The --log argument requires the --logpath parameter to be defined')
elif args.logpath != "--" and args.log == False:
    parser.error('The --logpath argument requires the --log parameter to be provided')
    exit

# Suppress all warnings
warnings.filterwarnings('ignore')

# HTTP Function
def httpTest():
# Get Current Timestamp
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y - %H:%M:%S")
# Get Status code from each URL passed in on the commandline    
    try:
        if(args.certcheck == False):
            uptime_check=requests.get(u, verify=False)
            uptime_check.raise_for_status()
            print(f"{current_time} - {u} - Success")
        else:
            uptime_check=requests.get(u)
            uptime_check.raise_for_status()
            print(f"{current_time} - {u} - Success")
    # Catch Exceptions
    except socket.error as exc:
        print(f"{current_time} - {u} - ERROR - Connection Issue:")
        print(exc)
        
        if args.log == True:
            logfile = open(f"{args.logpath}/py-connect-test.log", "a")
            logfile.write(f"{current_time} - {u} - ERROR - Connection Issue: {exc}")
            logfile.write("\n")
            logfile.close()
            
        if args.alerts == True:
            webhook_url = str(args.webhook_url)
            with open("/tmp/payload.json") as file:
                payload = json.load(file)
            try:
                response = requests.post(webhook_url, json=payload)
                print(payload)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"{current_time} - {u} - ERROR - Failed to call webhook:")
                print(e)
# Main Block
if len(args.urls) == 0:
    print("No URL Received, please use -h to see list of parameters")
# Call httpTest func
for u in args.urls:
    httpTest()
    time.sleep(180)