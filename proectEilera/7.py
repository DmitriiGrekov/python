

def prosoe_num(n):
    d=2

    while n%d!=0:
        d+=1

    return d==n




arr = []
i=2
while len(arr)<=10001:
    if prosoe_num(i):
        arr.append(i)
        print(arr)
    i+=1

print(arr)
