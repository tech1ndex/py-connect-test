import requests
from datetime import datetime
import time
import warnings
import sys

# Suppress all warnings
warnings.filterwarnings('ignore')


# While loop to run indefinitely 
while True:
    
    #Sleep for 5 Seconds in between checks
    time.sleep(15)
    
    #Get Current Timestamp
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y - %H:%M:%S")
    

    # Get Status code from each URL passed in on the commandline
    urls = sys.argv
    for u in urls[1:]:
        try:
            uptime_check=requests.get(u)
            uptime_check.raise_for_status()
        except requests.exceptions.RequestException as err:
        # Write to file if connection times out to URL
            uptime_status_code = str(uptime_check.status_code)
            logfile = open("/log/py-connect-test.log", "a") #adding local path for testing purposes 
            logfile.write(f"{current_time} - {u} - ERROR - Response: {uptime_status_code}")
            logfile.write("\n")
            logfile.close()