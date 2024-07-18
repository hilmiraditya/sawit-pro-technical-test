import os, sys

LOG_FILE = "sample.log"
BASE_DIRECTORY="log-categorized-status-code"
STATUS_CODES=[200, 201, 400, 401, 403, 404, 500, 502, 503]

def create_directory():
    for status_code in STATUS_CODES:
        os.makedirs(BASE_DIRECTORY+"/"+str(status_code), exist_ok=True)

def main():
    create_directory()

main()