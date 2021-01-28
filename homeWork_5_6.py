print("Урок 5 задача 6 - создать не программно файл, сформировать словарь, содержащий название предмета и количество общее занятий по нему, вывести на экран  \n")
print("Файл для работы textFhW5_6.txt \n")
with open ("textFhW5_6.txt", "r") as my_text:
    my_dict={}
    for line in my_text:
        my_list=line.split()
        print("Данные из файла\n\n ",my_list)
        ext_sum=0 
        for i in range(1,len(my_list)):
            my_int_list=my_list [i].split("(")
            ext_sum+=int(my_int_list[0])
        my_dict.update({my_list[0]:ext_sum})
    print("\n Полученный словарь \n\n",my_dict)