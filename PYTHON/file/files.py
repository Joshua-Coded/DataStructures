import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random data to test our file\n More random data to test\n and some more random data to test")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)


os.rename("mydata.txt", "data.txt")
os.remove("data.txt")

os.mkdir("mkdir")
os.chdir("mkdir")

print("Current directory :", os.getcwd())