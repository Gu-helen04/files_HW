from typing import List
def reading_file ():
    flag_end = True
    description_dish = []
    ingredient_dictionary = []
    list_ingredients = {}
    cook_book = {}
    with open('file.txt', encoding="utf-8") as file:
        while flag_end:
            file_line = file.readline()
            if not file_line:
                for ingredient_str in description_dish:
                    if description_dish.index(ingredient_str) > 1:
                        ingredient_dictionary_ = ingredient_str.split('|')
                        list_ingredients = {'ingredient_name': ingredient_dictionary_[0],
                                            'quantity': ingredient_dictionary_[1],
                                            'measure': ingredient_dictionary_[2]}
                        # print(list_ingredients)
                    if len(list_ingredients) != 0:
                        ingredient_dictionary.append(list_ingredients)
                # if description_dish[0] !=
                cook_book[description_dish[0]] = ingredient_dictionary
                description_dish = []
                ingredient_dictionary = []
                list_ingredients = {}
                flag_end = False
            else:
                if file_line != '\n':
                    description_dish.append(file_line.rstrip('\n'))
                else:
                    for ingredient_str in description_dish:
                        if description_dish.index(ingredient_str) > 1:
                            ingredient_dictionary_ = ingredient_str.split('|')
                            list_ingredients = {'ingredient_name': ingredient_dictionary_[0],
                                                'quantity': ingredient_dictionary_[1],
                                                'measure': ingredient_dictionary_[2]}
                            # print(list_ingredients)
                        if len(list_ingredients) != 0:
                            ingredient_dictionary.append(list_ingredients)
                    # if description_dish[0] !=
                    cook_book[description_dish[0]] = ingredient_dictionary
                    description_dish = []
                    ingredient_dictionary = []
                    list_ingredients = {}
        return cook_book
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = reading_file()
    temporary_list_adding_products ={}
    final_list = {}
    name_dish = ''
    product_measurement = ''
    amount = ''
    for dishes_ in dishes:
        for name_dish_,list_products in cook_book.items():
            if dishes_.lower() == name_dish_.lower():
                for ingridiets in list_products:

                    for key,value in ingridiets.items():
                        if key == 'ingredient_name':
                            name_dish = value
                        if key == 'measure':
                            product_measurement = value
                        if key == 'quantity':
                            amount = int(value) * int(person_count)
                        if amount and product_measurement and name_dish:
                            temporary_list_adding_products['measure'] = product_measurement
                            temporary_list_adding_products['quantity'] = amount
                            if not (name_dish in final_list):
                                final_list[name_dish] = temporary_list_adding_products
                                temporary_list_adding_products = {}
                                name_dish = ''
                                product_measurement = ''
                                amount = ''
                            else:
                                for key,value in final_list.items():
                                   if key == name_dish:
                                        initial_amount = int(value["quantity"])
                                        value["quantity"] = int(initial_amount) + int(amount)
                                        temporary_list_adding_products = {}
                                        name_dish = ''
                                        product_measurement = ''
    return (final_list)

if __name__ == '__main__':
    question_user = input(f'\nХотите рассчитать количество продуктов?\n(y/n)\n')
    if question_user.lower() == 'y':
        list_dish = []
        login_verification = False
        cook_book = reading_file()
        print('\nДоступны следующие блюда:')
        for key, value in cook_book.items():
            print(f'{key}')
        print(f'Введите список блюд через Enter\nДля остановки нажмите:S')
        check_flag = True
        while check_flag:
            data_input = input('ввод: ')
            if data_input != 's':
                for key_, value_ in cook_book.items():
                    if (key_.strip()).lower() == (data_input.strip()).lower():
                        login_verification = True
                if login_verification:
                    if data_input != 's':
                        if [] != list_dish:
                            for dishes_ in list_dish:
                                if not(dishes_ == data_input) and data_input != '':
                                    list_dish.append(data_input)
                                    data_input = ''
                                    login_verification = False
                        else:
                            list_dish.append(data_input)
                            data_input = ''
                            login_verification = False
                elif not login_verification:
                    print('Ошибка:Блюдо не найдено, проверте правильност ввода и повторите попытку')
            else:
                check_flag = False
        #print(list_dish)
        if  list_dish:
            try:
                number_dishes =int(input('Введите количество порций: '))
                if not (number_dishes <= 0):
                    calculation_result = get_shop_list_by_dishes(list_dish, number_dishes)
                    print('Для приготовления выббранных блюд, Вам понадобится:')
                    for key, value in calculation_result.items():
                        print(f'\n{key}\t{value}')
                else:
                    print('Ошика: Количество порций не может быть нулевым или отрицательным')
            except ValueError:
                print('Ошибка: Введено не числовое значение')
        else:
            print('Список блюд пуст')

    elif question_user.lower() == 'n':
        print('Пока-Пока')
    else:
        print('Ошибка ввода')

