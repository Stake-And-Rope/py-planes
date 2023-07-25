import json

def read_username():
    user_settings_file = open(r'settings/user_settings.json')
    user_data = json.load(user_settings_file)
    print(user_data['username'])
    
    
read_username()