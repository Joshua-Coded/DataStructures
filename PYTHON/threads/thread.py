import threading
import time
import random


def executeThread(i):
    print("Thread sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))

    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

    print("Thread Stops Sleeping at {}".format(i, time.strftime("%H:&M:%S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads : ", threading.activeCount())

    print(["Thread Objects : ", threading.enumerate()])


