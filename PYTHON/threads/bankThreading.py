import threading
import time
import random


class BankAccount(threading.Thread):

    accountBalance = 100

    def __init__(self, name, moneyRequest):
        threading.Thread.__init__(self)

        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()

        BankAccount.getMoney(self)

        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.moneyRequest,
                                                         time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.accountBalance - customer.moneyRequest > 0:
            BankAccount.accountBalance -= customer.moneyRequest
            print("New account balance : ${}".format(BankAccount.accountBalance))
        else:
            print("Not enough money to withdraw")
            print("New account balance : ${}".format(BankAccount.accountBalance))
        time.sleep(3)

threadLock = threading.Lock()

dough = BankAccount("Dough", 1)
paul = BankAccount("Dough", 100)
sala = BankAccount("Dough", 20)

dough.start()
paul.start()
sala.start()

dough.join()
paul.join()
sala.join()

print("Execution Ends")

