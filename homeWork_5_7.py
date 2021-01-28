import json
print("Урок 5 задача 7 - построчно прочитать файл, вычислить прибыль каждого и среднююс убытками в список не включать, итоговый список сохранить в json-обьект в   \n")
print("Файл для работы TextFhW5_7.txt \n")
with open ("TextFhW5_7.txt", "r") as my_text:
    my_list_general=[]
    my_dict_damage={}
    my_dict_profit={}
    print("Данные из файла\n ")
    for line in my_text:
        my_list=line.split()
        print (my_list) 
        gener_sum=0
        gener_count=0        
        my_balanse=int(my_list[2])-int(my_list[3])
        if my_balanse>=0:
            gener_sum+=my_balanse
            gener_count+=1
            my_dict_profit.update({my_list[0]:my_balanse})
        else:
            my_dict_damage.update({my_list[0]:my_balanse})
    my_dict_aver={"average profit":gener_sum / gener_count}
    my_list_general=[my_dict_profit, my_dict_aver, my_dict_damage]
    print ("\nТребуемый список \n\n", my_list_general) 
with open ("my_file.json", "w") as my_text_json:
    json.dump(my_list_general, my_text_json)
    print("\n Через json \n\n", json.dumps(my_list_general))
    
