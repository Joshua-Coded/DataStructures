import re

# if re.search("animal", "which of the following is an animal"):
#     print("We have animal in there")
# else:
#     print("not found")

# theStr = "The ape was at the apex"

# for i in re.finditer("ape.", theStr):
#     locTuple = i.span()

#     print(locTuple)
#     print(theStr[locTuple[0]:locTuple[1]])

# animalStr = "Cat, rat, mat, pat"

# allAnimals = re.findall("[crmtp]at", animalStr)

# for i in allAnimals:
#     print(i) 

# someAnimals = re.findall("[c-mC-M]at", animalStr)

# for i in someAnimals:
#     print(i)

# owlFood = "Rat, Cat, Mat, Pat"

# regex = re.compile("[CR]at")

# owlFood = regex.sub("owl", owlFood)
# print(owlFood)

# randStr = "Here is \\stuff"

# print("Find \\stuff :", re.search(r"\\stuff", randStr))

# randStr = "F.B.I. I.R.S CIA"

# print("Matched :", len(re.findall(".\..\..\.", randStr)))

# randStr = ''' this is a long 
# string that 
# goes on for many lines'''

# print(randStr)

# regex = re.compile("\n")

# randStr = regex.sub(" ", randStr)
# print(randStr)

# randStr = "12345"

# print("Matches : " , len(re.findall("\d", randStr)))
# print("Matches : " , len(re.findall("\d{5}", randStr)))

# numStr = "123 12345 123456 1234567"

# print("Matches : " , len(re.findall("\d{5,7}" , numStr)))

# phNum = "234-435-435-3323"

# if re.search("\w{3}-\w{3}-\w{4}", phNum):
#     print("That is a phone number") 

# if re.search("\w{2,20}", "newton"):
#     print("is a valid name")
# else:
#     print("is not a valid name")

# if re.search("\w{2,20}\s\w{2,20}", "the boy is good"):
#     print("great that is valid")
# else:
#     print("that is not great")

# print("Matches", len(re.findall("a+", "a as ape animal big")))