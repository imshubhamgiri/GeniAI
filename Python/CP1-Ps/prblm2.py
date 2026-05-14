import os

directory = '/webdev'

content = os.listdir(directory)

for item in content:
    print(item)