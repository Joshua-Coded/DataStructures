import threading
import time
import random

class CustomThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        getTime(self.name)

        print("Thread", self.name, "Execution Ends")


def getTime(name):
        print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))

        randSleepTime = random.randint(1, 5)

        time.sleep(randSleepTime)

thread1 = CustomThread("Computer 1")
thread2 = CustomThread("Computer 2")
thread3 = CustomThread("Computer 3")

thread1.start()
thread2.start()
thread3.start()

print("Thread 1 Alive : ", thread1.is_alive())
print("Thread 2 Alive : ", thread2.is_alive())
print("Thread 3 Alive : ", thread3.is_alive())

print("Thread 1 Name : ", thread1.name)
print("Thread 2 Name : ", thread2.name)
print("Thread 3 Name : ", thread3.name)

thread1.join()
thread2.join()
thread3.join()

print("Execution Ends")
