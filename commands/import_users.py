from services.users import fetch_users
import csv

def handle(command):
    print(command)
    
    users = fetch_users()
    with open("users.csv", "w", newline="", encoding="utf-8") as users_file:
        users_writer=csv.writer(users_file)
        for user in users:
            users_writer.writerow(user)
        
    
    