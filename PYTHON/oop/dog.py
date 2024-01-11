class Dog:

    def __init__(self, name="", height=0, width=0):
        self.name = name
        self.height = height
        self.width = width

    def run(self):
        print("{} the dog runs".format(self.name))

    
    def eat(self):
        print("{} the dog runs".format(self.name))
    
    def barks(self):
        print("{} the dog runs".format(self.name))


def main():
    spot = Dog("Spot", 44, 45)
    spot.run()




main()
