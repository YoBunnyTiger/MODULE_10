from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.warriors = 100
        self.day = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warriors != 0:
            self.warriors -= self.power
            sleep(1)
            self.day += 1
            print(f"{self.name}, сражается {self.day} день(дня)..., осталось {self.warriors} воинов.")
        else:
            print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
