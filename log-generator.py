import random
from datetime import datetime

# This file will be generate random logs
# Log Format: 
# [timestamp] [service_name] [status_code] [response_time_ms] [user_id] [transaction_id] [additional_info]

# Constants
LOG_LINES = 1000
LOG_FILE = "sample.log"
STATUS_CODES = [200, 201, 400, 401, 403, 404, 500, 502, 503]
SERVICE_NAMES = ["sawitpro-auth", "sawitpro-payment", "sawitpro-inventory", "sawitpro-order", "sawitpro-shipping"]
ADDITIONAL_INFO = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

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
    return random.choice(ADDITIONAL_INFO)

def generate_log():
    return "[" + get_timestamp() + "] " + get_service_name() + " " + get_status_code() + " " + get_response_time() + " " + get_user_id() + " " + get_transaction_id() + " [User Agent: " + get_additional_info() + "]\n"

def main():
    log_file = open(LOG_FILE, "a")
    log_line = 1

    while log_line <= LOG_LINES:
        log_file.write(generate_log())
        log_line += 1
    
    log_file.close()

main()