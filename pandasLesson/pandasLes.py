import numpy as np
import pandas as pd
import random


s1 = pd.Series([i for i in range(random.randint(0,100),random.randint(101,1000))])

print(s1)


ndarr=np.array([1,3,4,5,6])
s2 = pd.Series(ndarr,['a','b','c','d','e'])
print(s2)


d = {"price":pd.Series([1, 2, 3], index=['v1', 'v2', 'v3']),"count": pd.Series([10, 12, 7], index=['v1', 'v2', 'v3'])}


df1 = pd.DataFrame(d)
print(df1)


d2 = {"price":np.array([1, 2, 3]),"count": np.array([10, 12, 7])}

df2 = pd.DataFrame(d2,index=['v1','v2','v3'])
print(df2)
