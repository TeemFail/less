print("Урок 5 задача 2 - создать не программно текстовый файл, записать в него несколько строк, подсчитать количество строк и слов \n")
my_lines=0
my_words=1
with open ("Test2.txt", "r") as my_text:
    for line in my_text:
        my_lines+=1
        for letter in line:
            if letter == " ":
                my_words+=1
print(f"Количество строк {my_lines} количество слов {my_words}")
                
