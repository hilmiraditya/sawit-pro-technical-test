import os, sys

LOG_FILE = "sample.log"
BASE_DIRECTORY="log-categorized-status-code"
STATUS_CODES=[200, 201, 400, 401, 403, 404, 500, 502, 503]

def create_directory():
    os.makedirs(BASE_DIRECTORY, exist_ok=True)
    for status_code in STATUS_CODES:
        log_file = open(BASE_DIRECTORY+"/"+str(status_code)+".log", "a")
        log_file.close()

def main():
    create_directory()

main()