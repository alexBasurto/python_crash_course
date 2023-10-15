import json

numbers = [2, 3, 5, 7, 11, 13, 18]

filename = 'cap10\\numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)