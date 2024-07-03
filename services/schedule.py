from datetime import datetime, timedelta
import csv 
from services.users import read_users

def read_last_date():
    try:
        with open('schedule.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if rows:
                last_row = rows[-1]
                last_date = datetime.strptime(last_row[0], '%Y-%m-%d')
                return last_date
            else:
                return None
    except FileNotFoundError:
        return None

def generate_schedule():
    last_date = read_last_date()
    current_date = last_date or datetime.today() + timedelta(days=1)
    end_date = datetime.today() + timedelta(days=30)
    users = read_users()
    current_user_index = 0
    
    with open('schedule.csv', 'a', newline='') as schedule_file:
        writer = csv.writer(schedule_file)
        while current_date <= end_date:
            # if current_date is not a weekday continue
            if current_date.weekday() >= 5:
                current_date += timedelta(days=1)
                continue
            current_user = users[current_user_index]
            current_user_index = (current_user_index + 1) % len(users)
            writer.writerow([current_date.strftime('%Y-%m-%d'), *current_user])
            current_date += timedelta(days=1)


        