import os

def number_of_lines_in_file(name_files):
    with open(name_files, encoding="utf-8") as file:
        flag_end = True
        line_counter = 0
        while flag_end:
            file_line = file.readline()
            if file_line:
                line_counter +=1
            else:
                flag_end = False
    return (line_counter)

def retrieve_file_content(name_files):
    with open(name_files, encoding="utf-8") as file:
        text_files = file.read()
    return (text_files)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #number_files_in_folder = (len(glob.glob('*.txt')))
    name_files = ['1.txt','2.txt', '3.txt']
    array_number_lines_in_files = []
    temporary_tring_for_text = ''
    for file in name_files:
        array_number_lines_in_files.append(number_of_lines_in_file(file))
    array_number_lines_in_files.sort()
    for file_length in array_number_lines_in_files:
        for name_file_ in name_files:
            if file_length == number_of_lines_in_file(name_file_):
                file_contents = retrieve_file_content(name_file_)
                if  temporary_tring_for_text:
                    temporary_tring_for_text = temporary_tring_for_text+'\n' + name_file_ + '\n' + str(file_length) + '\n' + file_contents + '\n'
                else:
                    temporary_tring_for_text = name_file_ + '\n' + str(file_length) + '\n' + file_contents + '\n'
    name_new_files = input(f'Введите имя нового файля:  ')+'.txt'
    if not(os.path.exists(name_new_files+'.txt')):
        file = open(name_new_files, "w")
        file.write(temporary_tring_for_text)
        file.close()
        print('Фаил создан')
    else:
        print('ОШИБКА: Документ с таким именем уже существует')
    #print(new_Stroka)

    #print(number_files_in_folder)
    #print(f'{number_of_lines_in_file("1.txt")}\n{number_of_lines_in_file("2.txt")}\n{number_of_lines_in_file("3.txt")}\n')
    #print(f'{retrieve_file_content("1.txt")}\n{retrieve_file_content("2.txt")}\n{retrieve_file_content("3.txt")}\n')


