import re

randStr = "<name>Life on mars</name><name>Freaks and geek</name>"

regex = re.compile("<name>.*?</name>")

match = re.findall(regex, randStr)

for i in match:
    print(i)