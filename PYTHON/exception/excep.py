try:
    aList = [1,2,3]

    print(aList[3])

except IndexError:
    print("Sorry that index does not exist")

except:
    print("Sorry Unknown error occurred")