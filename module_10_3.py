from threading import Thread, Lock
from time import sleep
import random

import lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for trans in range(100):
            # with self.lock:
            random_num = random.randint(50, 500)
            self.balance += random_num
            print(f"Пополнение: {random_num}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for trans in range(100):
            # with self.lock:
            random_num = random.randint(50, 500)
            print(f'Запрос на {random_num}')
            if random_num <= self.balance:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            elif random_num > self.balance:
                self.lock.acquire()
                print(f'Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
