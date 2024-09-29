def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for file.readline in file:
            all_data.append(file.readline)
    with open('file.txt', 'w', encoding='utf-8') as info:
        info.write(str(all_data))



if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    # for i in filenames:
    read_info(filenames[1])
