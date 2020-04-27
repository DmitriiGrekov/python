num  = int(input())
arr = []
for i in range(1,num):
    if num%i ==0:
        arr.append(i)


def IsPrime(n):
        d = 2
        while n % d != 0:
            d += 1
        return d == n
s=[]
for i in arr:
    if IsPrime(i):
        s.append(i)
print(s)

