print("Урок 5 задача 4 - создать не программно текстовый файл с указанным содержимым, открыть и прочитать построчно, заменить английские числительные на русские, новые строки записывать в новый файл  \n")
print("Файл для работы Numbers.txt и Numbers2 \n")
my_dict={"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
with open ("Numbers.txt", "r") as my_text:
    for line in my_text:
        my_line = line.split()
        my_line[0]=my_dict.get(my_line[0])
        with open ("Numbers2.txt","a") as my_text2:
            my_text2.write(" ".join(my_line)+"\n")
with open ("Numbers2.txt") as my_text:
    for line in my_text:
        print(line)
