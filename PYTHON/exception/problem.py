# Create a file named mydata2.txt
# Find out hoe to open a file without with (Open in try)
# Catch FileNotFoundError
# In else print contents
# In finally
# Open nonexistent file mydata3.txt

try:
    myFile = open("mydata2.txt", encoding="utf-8")

except FileNotFoundError as ex:
    print("File not found")

    print(ex.args)

else:
    print("File : ", myFile.read())
    myFile.close()

finally:
    print("Done working with file")