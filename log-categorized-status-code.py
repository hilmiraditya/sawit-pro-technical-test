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

def write_file(directory, line):
    file=open(directory, "a")
    file.write(line)
    file.close()

def activity_count(activity):
    activity_counts[activity] = activity_counts[activity] + 1

def status_code_count(status_code):
    status_code_counts[status_code] = status_code_counts[status_code] + 1
    
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
                activity_count("purchase")
                write_file(ACTIVITY_BASE_DIRECTORY+"/purchase.log", log)
        
            elif "view" in log_splits[7]:
                activity_count("view")
                write_file(ACTIVITY_BASE_DIRECTORY+"/view.log", log)

            elif "return" in log_splits[7]:
                activity_count("return")
                write_file(ACTIVITY_BASE_DIRECTORY+"/return.log", log)

def main():
    check_sample_log_file()
    initiate_directory(STATUS_CODE_BASE_DIRECTORY)
    initiate_directory(ACTIVITY_BASE_DIRECTORY)
    parse_logs()
    print(status_code_counts)
    print(activity_counts)

main()