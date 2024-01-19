import re

# randStr = "<name>Life on mars</name><name>Freaks and geek</name>"

# regex = re.compile("<name>.*?</name>")

# randStr = "ape at the apex"

# regex = re.compile(r"\bape\b")

# randStr = "match everything up to the @"

# regex = re.compile(r"^.*[^@]")


# randStr = "@ get this string"

# regex = re.compile(r"[^@\s].*$")


randStr = '''Ape is big
Turtle is slow
cheetah is fast
'''

regex = re.compile(r"(?m)^.*?\s")

match = re.findall(regex, randStr)

for i in match:
    print(i)