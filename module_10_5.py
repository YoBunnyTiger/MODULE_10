from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

#  Линейный вызов
    start = datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.now() - start
    print(f'{end} (линейный)')

# Многопроцессный вызов
    start = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.now() - start
    print(f'{end} (многопроцессный)')
