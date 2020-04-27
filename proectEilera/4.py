arr = []
for i in range(10,100):
    for j in range(10,100):
        arr.append(i*j)


news=[]

for i in arr:
    a = str(i)

    
    if i ==  int(a[::-1]) :
        news.append(i)


print(news)
