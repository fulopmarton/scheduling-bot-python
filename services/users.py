from lib.slack_app import app
import csv

def fetch_users():
    users = app.client.users_list()['members']   
    users_parsed = [(user['id'], user['name'], user['real_name']) for user in users if (not user['is_bot'])]
    return users_parsed
    
def read_users():
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        users = list(reader)
    return users
