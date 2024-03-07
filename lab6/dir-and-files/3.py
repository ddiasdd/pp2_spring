import os

print("Test a path exists or not:")
path = r'/Users/apple/Desktop/pp2_spring'
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))

print("Test a path exists or not:")
path = r'D:\\epicGames\\Tunche.exe'
print(os.path.exists(path))

print("\nFile name of the path:")
print(os.path.basename(path))

print("\nDir name of the path:")
print(os.path.dirname(path))