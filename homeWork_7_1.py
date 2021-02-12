print("""Урок 7 задача 1 - 
реализовать класс Matrix, обеспечить
перезагрузку __init__ принимает список
списков для формирования матрицы
реализовать перегрузку __str__ для
вывода матрицы в привычном виде
реализовать перегрузку __add__ для 
сложения 2х обьектов класса (двух матриц)
результат - новая матрица \n""")

class Matrix:
    def __init__(self, m_lists=None):
        self.m_lists = list(m_lists)
        
#распечатка без __str__ в привычном виде        
    #def pr_matr(self, m_lists):
        #for i in range(len(self.m_lists)):
            #print(self.m_lists[i])
#m.pr_matr(([1, 2, 3], [3, 4, 5], [6, 7, 8]))
            
# печать в начальном виде списка списков    
    def m_result(self):
        return(self.m_lists)
        
        
    def __str__(self):
        return f'в привычном виде \n {" ".join(map(str, self.m_lists[0]))} \n {" ".join(map(str, self.m_lists[1]))} \n {" ".join(map(str, self.m_lists[2]))} \n'
        
        
    def __add__(self, other):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.m_lists)):
            for j in range(len(self.m_lists[i])):
                result[i][j] = self.m_lists[i][j]+other.m_lists[i][j]
        return Matrix(result)
        
           
        
matr_1 = Matrix(([1, 2, 3], [3, 4, 5], [6, 7, 8]))

print("Вывод списка списков: \n", matr_1.m_result())
print("Матрица 1 \n", matr_1)

matr_2 = Matrix(([3, 2, 1], [5, 4, 3], [8, 7, 6]))
print("Матрица 2 \n", matr_2)

matr_3 = (matr_1 + matr_2)
print("Матрица сложения \n", matr_3)