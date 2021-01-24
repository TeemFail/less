print(
    "Функция принимает положительный х и отрицательный у и возвращает х в степени у без применения встроенных функций \n")


def my_funk(var_1, var_2):
    print(f"Число {var_1} в степени {var_2}")
    var_3 = 1 / (var_1 ** abs(var_2))
    return var_3


print("(Через **)", round(my_funk(3, -2), 3))

print("\n Теперь через цикл")


def my_sqrt(var_1, var_2):
    p = 1
    for i in range(abs(var_2)):
        p *= var_1
    return 1 / p


print("(Через цикл)", round(my_sqrt(3, -2), 3))
