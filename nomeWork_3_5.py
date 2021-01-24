print(
    "Запрос строки чисел разделенных пробелом. Вывод суммы. Продолжение ввода. Если введен символ n прекратить ввод. Сумма постоянно растет \n")


def my_funk():
    i = 1
    my_list_sum = []
    while i == 1:
        user_input = input(
            "Введите числа, разделенные пробелом, прекрашение работы - n в любом месте последовательности: ")
        my_list = user_input.split()
        for n in my_list:
            if n == "n":
                i += 1
                break
            else:
                my_list_sum.append(int(n))
    my_list_sum = sum(my_list_sum)
    return my_list_sum


print(my_funk())
