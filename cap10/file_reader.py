file_path = 'C:\www\python_work\cap10\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())