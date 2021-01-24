print("Функция принимает текст маленькими латинскими буквами и возвращает с первой прописной буквой \n")
print("Первая часть задания \n")
user_text = input("Введите слово маленькими латинскими буквами: ")


def my_funk(user_text):
    my_text = user_text.title()
    return my_text


print(my_funk(user_text))

print("Вторая часть задания \n")
my_line_answr = []
user_text = input("Введите текст маленькими латинскими буквами через пробел: ")
my_line = user_text.split()
my_line_answr.append(my_funk(user_text))
print(" ".join(my_line_answr))
