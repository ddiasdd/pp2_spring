import os

print('Exist:', os.access('/Users/apple/Desktop/pp2_spring/test.txt', os.F_OK))
print('Readable:', os.access('/Users/apple/Desktop/pp2_spring/test.txt', os.R_OK))
print('Writable:', os.access('/Users/apple/Desktop/pp2_spring/test.txt', os.W_OK))
print('Executable:', os.access('/Users/apple/Desktop/pp2_spring/test.txt', os.X_OK))