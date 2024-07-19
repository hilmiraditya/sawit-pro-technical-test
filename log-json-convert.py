import os
import json

LOG_FILE="sample.log"
JSON_FILE="sample-log.json"

json_write=[]

def check_sample_log_file():
    if not os.path.exists(LOG_FILE):
        raise Exception(LOG_FILE + " file not available")
    
def parse_logs():
    with open(LOG_FILE, "r") as logs:
        for log in logs:
            log_splits=log.split()
            timestamp = log_splits[0]+" "+log_splits[1]
            
            data_log = {
                "timestamp": timestamp,
                "service_name": log_splits[2],
                "status_code": log_splits[3],
                "response_time": log_splits[4],
                "user_id": log_splits[5],
                "transaction_id": log_splits[6],
                "activity": log_splits[7]
            }

            json_write.append(data_log)
        
        with open(JSON_FILE, 'a') as json_file:
            json.dump(json_write, json_file,indent=4)

        
def main():
    check_sample_log_file()
    parse_logs()

main()