with open("../requirement.txt", "r") as file:
    for line in file.readlines():
        print("pip install " + line.replace("\n", "") + ";")