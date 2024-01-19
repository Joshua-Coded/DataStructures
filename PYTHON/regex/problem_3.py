import re

# randStr = "https://www.youtube.com http://www.google.com"

# # sample output
# # <a href="https://www.youtube.com">www.youtube.com</a>
# #<a href="https://www.google.com">www.google.com</a>

# # Solution

# regex = re.compile(r"(https?://([\w.]+))")

# randStr = re.sub(regex, r"<a href='\1'>\2</a>\n", randStr)
# print(randStr)

# randStr = "1. Dog 2. Cat 3. Turtle"

# regex = re.compile(r"\d\.\s(Dog | Cat)")

# matches = re.findall(regex, randStr)

# for i in matches:
#     print(i)

# randStr = "12345 12345-1234 1234 12346-333"

# regex = re.compile(r"(\d{5}-\d{4} | \d{5} \s)")

# matches = re.findall(regex, randStr)

# for i in matches:
#     print(i)


bd = input("Enter your birthday (mm-dd-yyyy) : ")

bdRegx = re.search(r"(\d{1,2})-(\d{1,2})-(\d{4})", bd)

print("You were born on", bdRegx.group())

