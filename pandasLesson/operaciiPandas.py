import pandas as pd
import numpy as np



d = {'price':np.array([5,3,4,2]),'count':np.array([6,4,2,1])}

df1 = pd.DataFrame(d,index=['a','b','c','d'])


print(df1)


print(df1['count'])  #выбор столбца

print(df1.loc['b'])  #выбор строки b
print()
print(df1[0:2])     #Выбираем первые 2 строки


https://devpractice.ru/pandas-indexing-part3/
