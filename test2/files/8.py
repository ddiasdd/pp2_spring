import os
x = "B.txt"
if os.path.exists(x):
    os.remove(x)
else:
    print("No")
