def is_simple(n):
    d=2


    while n%d!=0:
        d+=1

    return d==n



arr = []
i=2
while i<=2000000:
    if is_simple(i):
        arr.append(i)
    


    i+=1



print(arr)


print()

print(sum(arr))

