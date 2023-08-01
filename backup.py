import shutil
import schedule
import time
import os

from datetime import datetime

def copy_folder(source_dir, destination_dir):
    try:
        shutil.copytree(source_dir, destination_dir)
        print(f"Folder copied from '{source_dir}' to '{destination_dir}'")
    except Exception as e:
        print(f"Failed to copy folder: {e}")

def schedule_folder_copy(source_dir, destination_dir, schedule_time):
    schedule.every().day.at(schedule_time).do(copy_folder, source_dir, destination_dir)

if __name__ == "__main__":
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    source_directory = "hehehe"
    destination_directory = "put/backup_"+dt_string
    scheduled_time = "15:14"

    schedule_folder_copy(source_directory, destination_directory, scheduled_time)

    while True:
        print(now)
        schedule.run_pending()
        print('loading')
        time.sleep(1)