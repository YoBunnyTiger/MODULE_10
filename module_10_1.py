from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for count in range(1, word_count + 1):
            file.write(f'Какое-то слово № {count}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()  # Время начала работы функции

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()  # Время окончания работы функции
print(f'Работа потоков {time_end - time_start}')

time_start = datetime.now()  # Время начала работы потоков

five = Thread(target=write_words, args=(10, 'example5.txt'))
six = Thread(target=write_words, args=(30, 'example6.txt'))
seven = Thread(target=write_words, args=(200, 'example7.txt'))
eight = Thread(target=write_words, args=(100, 'example8.txt'))

five.start()
six.start()
seven.start()
eight.start()

five.join()
six.join()
seven.join()
eight.join()

time_end = datetime.now()  # Время окончания потоков
print(f'Работа потоков {time_end - time_start}')
