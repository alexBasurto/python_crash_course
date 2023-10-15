import json

filename = 'cap10\\username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")