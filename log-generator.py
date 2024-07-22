import random
from datetime import datetime
import time
import sys
# This file will be generate random logs
# Log Format: 
# [timestamp] [service_name] [status_code] [response_time_ms] [user_id] [transaction_id] [additional_info]

# Constants
LOG_LINES = 1000
LOG_FILE = "sample.log"
STATUS_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]
SERVICE_NAMES = ["auth", "payment", "checkout", "logistic"]
ACTIVITIES= ["purchase", "view", "return"]
ITEMS = ["iPhone", "Xiaomi", "Samsung", "Oppo", "Realme", "Vivo"]

def get_timestamp():
    return str(datetime.now())

def get_service_name():
    return random.choice(SERVICE_NAMES)

def get_status_code():
    return str(random.choice(STATUS_CODES))

def get_response_time():
    # This function will be generate random response time, fyi: 
    # 1. Good response time: less than 200 ms
    # 2. Medium response time: between 200 ms and 1000 ms
    # 3. Low response time: more than 1000 ms
    return str(random.randint(100,5000)) + "ms"

def get_user_id():
    # User ID will be formatted : user_<random_id>
    return "user_" + str(random.randint(0,300))

def get_transaction_id():
    # User ID will be formatted : transaction_<random_id>
    return "transaction_" + str(random.randint(0,300))

def get_additional_info():
    return random.choice(ACTIVITIES)+"_"+random.choice(ITEMS)

def generate_log():
    log_file = open(LOG_FILE, "a")
    log_line = 1
    while log_line <= LOG_LINES:
        log_sample="[" + get_timestamp() + "] " + get_service_name() + " " + get_status_code() + " " + get_response_time() + " " + get_user_id() + " " + get_transaction_id() + " " + get_additional_info() + "\n"
        log_file.write(log_sample)
        log_line += 1
    
    log_file.close()

    print(get_timestamp()+" sample request generated, "+str(LOG_LINES)+" lines.")


def main():
    args = sys.argv[1:]

    if len(args) == 2 and args[0] == "-interval":
        interval=args[1]
        print(get_timestamp()+" generate log with interval "+interval+"s")
        while(True):
            generate_log()
            time.sleep(int(interval))
    else:
        print(get_timestamp()+" generate log")
        generate_log()

main()