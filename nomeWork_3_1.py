print("Функция принимает данные, проверяет деление на ноль и выводит результат, если не ноль\n")

def my_funk(a = int(input ("Введите число ")), b = int(input ("Введите еще число "))):
    if b == 0:
        mess = "Невозможно делить на ноль"
        return mess
    else:
        c = a / b
        return round(c,3)


print ("\n", my_funk())


	 