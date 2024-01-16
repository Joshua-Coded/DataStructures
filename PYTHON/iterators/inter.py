# sampStr = iter("Samples")

# print("Char : ", next(sampStr))
# print("Char : ", next(sampStr))
# print("Char : ", next(sampStr))
# print("Char : ", next(sampStr))

class Alphabet:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.letters) - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.letters[self.index]
    

alpa = Alphabet()

for letter in alpa:
    print(letter)


    
