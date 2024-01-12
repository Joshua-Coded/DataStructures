# class Sum:

#     @staticmethod
#     def getSum(*args):
        
#         sum = 0

#         for i in args:
#             sum += i
#         return sum

# def main():
#     print(" Sum : ", Sum.getSum(1,2,3,4,5,5,6,))
# main()

class Dog:

    num_of_nums = 0

    def __init__(self, name="Uknown"):
        self.name = name

        Dog.num_of_nums += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_nums))
def main():

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()
main()