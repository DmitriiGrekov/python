a=[5,3,'hello',[3,4],' word',[6],10.6]



s_strok = ''
s_list = []
summ = 0
for i in a:
    if isinstance(i,str):
        s_strok=s_strok+i
    elif isinstance(i,list):
        s_list=s_list+i
    elif isinstance(i,int):
        summ+=i



print(s_strok)
print(s_list)
print(summ)
