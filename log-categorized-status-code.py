import os

LOG_FILE = "sample.log"
BASE_DIRECTORY="log-categorized-status-code"
STATUS_CODES=[200, 201, 400, 401, 403, 404, 500, 502, 503]


def initiate_directory():
    os.makedirs(BASE_DIRECTORY, exist_ok=True)

def read_files():
    with open(LOG_FILE, "r") as logs:
        for log in logs:
            log_splits=log.split()
            log_file=open(BASE_DIRECTORY+"/"+log_splits[3]+".log", "a")
            log_file.write(log)
            log_file.close()

def main():
    initiate_directory()
    read_files()

main()