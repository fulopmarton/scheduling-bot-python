import schedule
import threading
import time
from datetime import datetime
import csv
from services.schedule import generate_schedule
from lib.slack_app import app

def find_current_worker(date):
    # if date is not weekday return none
    if datetime.strptime(date, "%Y-%m-%d").weekday() > 4:
        return None
    for _ in range(2):
        with open('./schedule.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            
            for row in reader:
                print(row, date)
                if row[0] == date:
                    return row
        # we havent found the row,
        # regenerate csv
        generate_schedule(datetime.strptime(date))
    return None

def job(*args):
    # current_date = datetime.now().date()
    current_date = datetime.strptime("2024-10-14", "%Y-%m-%d")
    print(f"Current date {current_date}")
    worker = find_current_worker(current_date.strftime("%Y-%m-%d"))
    if not worker:
        print(f"No worker for {current_date}")
        return
    print(worker)
    print('worker', worker)
    print("Running job", args)
    resp = app.client.chat_postMessage(
        channel=worker[1],
        text="You are on duty today"
    )
    print(resp)

# Spawn a thread and runs scheduled jobs on that thread
def run_scheduler():
    print("Starting scheduler")
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    
def initialize():
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
