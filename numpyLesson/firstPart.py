import numpy as np


a = np.array([1,4,5,6],float)

b = np.array([[5,3,4,5],[2,3,45,6]],float)
print(b.shape) #выводит кол-во строк и столбцов

print()
c = np.array([1,2,3,4,5,6,7,8,9,10],float)

c = c.reshape(5,2)  #создаёт новый массив из элементов массива С с кол-вом строк 5 и столбцов 2
print(c)

print()

a = np.array([1,2,3],float)  
a.fill(0)    #заполняет массив нулями

print(a)

print()
a = np.array(range(6),float).reshape(2,3)

print(a.T)  #транспонирование

print()



a = np.array([[1, 2, 3], [4, 5, 6]], float)

a = a.flatten()   #конвертирует многомерный массив в одномерный
print(a)

print()

print(np.pi)



