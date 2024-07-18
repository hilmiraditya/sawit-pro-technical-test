import os

LOG_FILE = "sample.log"
STATUS_CODE_BASE_DIRECTORY="status-code-log"
ACTIVITY_BASE_DIRECTORY="activity-log"

status_code_counts = {
    200 : 0,
    201 : 0,
    400 : 0,
    401 : 0,
    403 : 0,
    404 : 0,
    500 : 0,
    502 : 0,
    503 : 0,
}

activity_counts = {
    "purchase" : 0,
    "view": 0,
    "return": 0
}

def check_sample_log_file():
    if not os.path.exists(LOG_FILE):
        raise Exception(LOG_FILE + " file not available")

def initiate_directory(directory):
    return os.makedirs(directory, exist_ok=True)
    
def parse_logs():
    with open(LOG_FILE, "r") as logs:
        for log in logs:
            log_splits=log.split()
            
            status_code=int(log_splits[3])
            status_code_counts[status_code] = status_code_counts[status_code] + 1

            status_code_log_file=open(STATUS_CODE_BASE_DIRECTORY+"/"+log_splits[3]+".log", "a")
            status_code_log_file.write(log)
            status_code_log_file.close()

            if "purchase" in log_splits[7]:
                activity_counts["purchase"] = activity_counts["purchase"] + 1
                activity_log_file=open(ACTIVITY_BASE_DIRECTORY+"/purchase.log", "a")
                activity_log_file.write(log)
                activity_log_file.close()
        
            elif "view" in log_splits[7]:
                activity_counts["view"] = activity_counts["view"] + 1
                activity_log_file=open(ACTIVITY_BASE_DIRECTORY+"/view.log", "a")
                activity_log_file.write(log)
                activity_log_file.close()

            elif "return" in log_splits[7]:
                activity_counts["return"] = activity_counts["return"] + 1
                activity_log_file=open(ACTIVITY_BASE_DIRECTORY+"/return.log", "a")
                activity_log_file.write(log)
                activity_log_file.close()

def main():
    check_sample_log_file()
    initiate_directory(STATUS_CODE_BASE_DIRECTORY)
    initiate_directory(ACTIVITY_BASE_DIRECTORY)

    parse_logs()
    print(status_code_counts)
    print(activity_counts)
    # count_results()

main()