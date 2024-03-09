import os
path_to = ''
print("Directions:")
for i in path_to:
    if os.path.isdir(i):
        print(i)
print("files:")
for i in path_to:
    if os.path.isfile(i):
        print(i)
print("all:")
print(path_to)
    