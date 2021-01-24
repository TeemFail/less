print("Функция принимает данные пользователя и выводит одной строкой\n")

def my_funk(name=input("Имя ?"), sname=input("Фамилия ?"), birth=input("Год ?"), city=input("Город ?"), eml=input("e-mail ?"), phone=input("Телефон ?")):
    return f"Имя {name} фамилия {sname} год рождения {birth} город {city} почта {eml} телефон {phone}"
    
    
print (my_funk())
    
    



	 