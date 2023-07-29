#!/bin/python3

import requests
from datetime import datetime
import time
import warnings
import argparse
import socket

# Parse Arguments
parser = argparse.ArgumentParser(description='A simple HTTP connection tester written in Python.')
parser.add_argument("-u", "--urls", help="A list of URLs to test against", nargs='*')
parser.add_argument("-l", "--log", help="Use --log if you want output logged to a file, default is stdout", action="store_true")
parser.add_argument("-p", "--logpath", help="Directory path to store logfile", default="--")
parser.add_argument("-i", "--interval", help="Interval at which to run the test in seconds, default value is 30", type=int, default=30)
parser.add_argument("--ssl", help="Use to toggle ssl certificate validation, default is to verify.", action=argparse.BooleanOptionalAction)
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
        if(args.ssl == False):
            uptime_check=requests.get(u, verify=False)
            uptime_check.raise_for_status()
            print(f"{current_time} - {u} - Success")
        else:
            uptime_check=requests.get(u)
            uptime_check.raise_for_status()
            print(f"{current_time} - {u} - Success")
    except socket.error as exc:
        print(f"{current_time} - {u} - ERROR - Connection Issue:")
        print(exc)
        if args.log == True:
            logfile = open(f"{args.logpath}/py-connect-test.log", "a") #adding local path for testing purposes 
            logfile.write(f"{current_time} - {u} - ERROR - Connection Issue: {exc}")
            logfile.write("\n")
            logfile.close()

# Main Block
while True:
    if len(args.urls) == 0:
        print("No URL Received, please use -h to see list of parameters")
        break
    # Call httpTest func
    for u in args.urls:
      httpTest()
                
    #Sleep for time defined in Interval flag
    time.sleep(args.interval)