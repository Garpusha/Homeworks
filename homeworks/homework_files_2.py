files = ['1.txt', '2.txt', '3.txt']
path = 'files_Task_2\\'
content = []

for index, file in enumerate(files):
    content.append([line.strip('\n') for line in open(path + file, 'r', encoding='utf-8')])
    content[index].insert(0, len(content[index]))
    content[index].insert(1, file)

content.sort()
result_file = open(path + 'result.txt', 'w', encoding='utf-8')

for file in content:
    result_file.write(f'Имя файла: {file[1]}\n')
    result_file.write(f'Количество строк: {file[0]}\n')
    for counter in range(2, file[0] + 2):
        result_file.write(f'{file[counter]}\n')
    result_file.write('\n')
result_file.close()
