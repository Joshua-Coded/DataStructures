import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some random data to test our file\n More random data to test\n and some more random data to test")

with open("mydata.txt", encoding="utf-8") as myFile:
    print(myFile.read())
