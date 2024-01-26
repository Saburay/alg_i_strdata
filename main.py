from sort_functions import *

def main():
    user_change = input(Fore.RESET + '\n[+] Выберите тип сортировки:\n   [1] Сортировка слиянием\n   [2] \n   '
                        '[3] \n   [4] \n   [5] \n'
                        '   [6] \n   [7] \n   '
                        '[8] \n   [9] Выход\n   >>> ')
    if user_change == "1":
        merge_sort(input('\n[+] Введите список: '))
    elif user_change == "2":
        pass
    elif user_change == "9":
        exit(0)
    else:
        print(Fore.RED + '\n[-] Неопознанный выбор. Повторите снова')
        main()



if __name__ == '__main__':
    main()