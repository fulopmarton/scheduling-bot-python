from lib.slack_app import app

def fetch_users():
    users = app.client.users_list()['members']   
    users_parsed = [(user['id'], user['name'], user['real_name']) for user in users if (not user['is_bot'])]
    return users_parsed
    
    