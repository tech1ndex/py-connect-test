#!/bin/python3

import requests
from datetime import datetime
import time
import warnings
import sys

# Suppress all warnings
warnings.filterwarnings('ignore')

# While loop to run indefinitely 
while True:
    

    
    #Get Current Timestamp
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y - %H:%M:%S")
    

    # Get Status code from each URL passed in on the commandline
    urls = sys.argv
    for u in urls[1:]:
        try:
            uptime_check=requests.get(u)
            uptime_check.raise_for_status()
            print(f"{current_time} - {u} - Success")
        except requests.exceptions.RequestException as err:
        # Write to file if connection times out to URL
            uptime_status_code = str(uptime_check.status_code)
            print(f"{current_time} - {u} - ERROR - Response: {uptime_status_code}")
        # Write error to logfile if parameter was defined    
            logfile = open(f"/log/py-connect-test.log", "a") #adding local path for testing purposes 
            logfile.write(f"{current_time} - {u} - ERROR - Response: {uptime_status_code}")
            logfile.write("\n")
            logfile.close()
                
    #Sleep for 30 Seconds in between checks
    time.sleep(30)