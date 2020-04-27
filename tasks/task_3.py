import time
text=''
with open('text.txt','r') as f:
    for s in f.readlines():
        arr = s.split()
        del_arr = {} 
        for i in range(len(arr)):
            if len(arr[i])>=3 and len(arr[i])<=5:
                del_arr[i] = arr[i]
        
        for k,v in del_arr.items():
            arr.remove(v) 

        text+=' '.join(arr)

print(text)

        

