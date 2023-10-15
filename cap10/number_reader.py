import json

filename = 'cap10\\numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)