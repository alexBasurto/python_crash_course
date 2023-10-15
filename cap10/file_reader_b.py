file_name = "cap10\\text_files\\socios.txt"

with open(file_name) as file_object:
    contents = file_object.read()
print(contents.rstrip())