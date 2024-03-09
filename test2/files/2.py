import os
path_to = r'/Users/apple/Desktop/test2/1.py'
print('Exist:', os.access(path_to, os.F_OK))
print('Readable:', os.access(path_to, os.R_OK))
print('Writable:', os.access(path_to, os.W_OK))
print('Executable:', os.access(path_to, os.X_OK))