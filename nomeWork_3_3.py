print("Функция принимает три позиционных аргумента и выдаёт сумму двух наибольших\n")


def my_funk(var_1=int(input("Введите число ")), var_2=int(input("Введите еще ")), var_3=int(input("И еще "))):
    var_4 = min(var_1, var_2, var_3)
    var_5 = (var_1 + var_2 + var_3) - var_4
    return var_5


print(my_funk())
