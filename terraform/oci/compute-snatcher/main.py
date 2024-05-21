import os
import requests
import json
import argparse
from datetime import datetime
from constants import BASE_DIRECTORY, SUBDIRS, LOGFILE, LOGFILE_ERROR

def send_message_to_webhook(webhook_url, message):
    """
    Sends a message to a webhook.

    Args:
        webhook_url (str): The URL of the webhook.
        message (str): The message to be sent.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        payload = {"text": message}
        headers = {"Content-Type": "application/json"}
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print("Message sent successfully.")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def write_to_file(file_path, content):
    """
    Writes content to a file with error handling.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write.

    Returns:
        bool: True if the write operation is successful, False otherwise.
    """
    try:
        with open(file_path, "a") as file:
            file.write(content + "\n")
        return True
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Script to apply Terraform configurations with optional checks.")
    args = parser.parse_args()

    for dir in SUBDIRS:
        log_dir = os.path.join(BASE_DIRECTORY, dir, "logs")
        timestamp = "Timestamp: {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        error_log_path = os.path.join(log_dir, LOGFILE_ERROR)
        log_path = os.path.join(log_dir, LOGFILE)

        if not write_to_file(error_log_path, timestamp):
            exit(1)

        if not write_to_file(log_path, timestamp):
            exit(1)

        os.chdir(os.path.join(log_dir, ".."))
        os.system(f"terraform apply -auto-approve -compact-warnings -no-color 2>> {error_log_path} 1>> {log_path}")

    exit()

if __name__ == "__main__":
    main()
 