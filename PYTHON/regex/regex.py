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

owlFood = "Rat, Cat, Mat, Pat"

regex = re.compile("[CR]at")

owlFood = regex.sub("owl", owlFood)
print(owlFood)