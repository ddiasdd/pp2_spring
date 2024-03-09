import os
def have(path):
    if os.path.exists(path):
        print("Yes file exists")
    else :
        print("No")