import re

# randStr = "<name>Life on mars</name><name>Freaks and geek</name>"

# regex = re.compile("<name>.*?</name>")

# randStr = "ape at the apex"

# regex = re.compile(r"\bape\b")

# randStr = "match everything up to the @"

# regex = re.compile(r"^.*[^@]")


# randStr = "@ get this string"

# regex = re.compile(r"[^@\s].*$")


# randStr = '''Ape is big
# Turtle is slow
# cheetah is fast
# '''

# randStr = "my number is 412-555-1212"

# randStr = "412-555-1212 412-555-6212 412-555-4212 412-555-1223"

# regex = re.compile(r"412-(.{8})")

# match = re.findall(regex, randStr)

# for i in match:
#     print(i)

# randStr = "the cat cat fell out the window"

# regex = re.compile(r"(\b\w+)\s+\1")

# match = re.findall(regex, randStr)

# for i in match:
#     print(i)

# randStr = "<a href='#'><b>The Link</b></a>"

# regex = re.compile(r"<b>(.*?)</b>")

# randStr = re.sub(regex, r"\1", randStr)
# print(randStr)


randStr = "412-555-1212"

regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")

randStr = re.sub(regex, r"(\1)\2", randStr)
print(randStr)