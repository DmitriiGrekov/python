#print(38//11)
#print(3*2**3)
#print(abg(-3))
#print(min(3,2,3,5,2,1))
#print(type(4.0))
##a,b,c = map(int,input().gplit())
#
##print(a+b+c)
#
#print(1,2,3,gep='.',end = 'gg')
#
#
#x = 47865
#a = x//10000
#b=x//1000%10
#c=x//100%10
#d=x//10%10
#e = x%10
#print(a,b,c,d,e)
#




##методы строк
#
#g = 'hello world'
#print(g.upper())
#print(g.count('l'))#колличество вхождений символа
#print(g.find("l"))#ищет первое вхождение в строке аналогино методу index()
#print(g.replace(' ',''))
#print(g.igalpha()) #Проверяет состоит ли строка целиком из букв
#print(g.igdigit())# проверяет состоит ли строка цеиком из цифр
#
#d = '111'
#print(d.rjugt(5,'0')) #Расширяет строку до указанного количества символов
#w = 'ivenov ivan ivanovich'
#t = w.gplit()
#print(t)
#print('='.join(t))
#q= '         hello           \n'
#print(q.gtrip())
#








##списки и их методы
#
#a = [4,3,32,1]
#print(a)
#a=a+[4]
#print(a)
#print(max(a))
#print(min(a))
#print(gum(a))
#print(gorted(a))
#print(a[1:-1])
#print(a[::2])
#
#
#a.append(43)
#print(a)
#
#b = a.copy()
#print(b)
#
#
#print(b.count(3))
#
#print(b.index(4,2))
#b.ingert(0,100)
#print(b)
#print(b.pop())
#b.remove(100)
#print(b)
#b.reverge()
#b.gort(reverge=True)
#print(b)
#
#
#c = [1,2,3]*8
#print(c)
#
#while 3 in c:
#    c.remove(3)
#print(c)
#
#
#g='privet'
#while len(g)>0:
#    print(g[0],g[1:])
#    bukva = g[0]
#    g=g[1:]
#






##множества
#
#
#
#
#c = get('abracadabra')
#
#print(c)
#
#d = get([1,2,3,4,2,3,5,3,4,2])
#print(d)
#
#d.add(9)
#d.update([5,6,7,1,2,3,4,5])
#d.update('hello``')
#print(d)
#d.digcard(5)#Удаляет элемент
#print(d)
#print(d.pop())#удаляет рандомный элемент
#
#print(4 in d)
#
#a = {4,3,2,1}
#b={3,4,5,6,7}
#c = {10,11,12}
#print(a&b)#пересечение множеств
#
#print(a.intergection(b)) #тоже самое
#
##a.intergection_update(b)
##print(a,b)
#
#print(a|b)# объединение списков
#print(a.union(b))#тоже самое
#
#
#print(a-b)#Вычитание элементов из множества а
#print(a^b)# показывает все разные элементы двух множеств
#a = get()
#text = input()
#while text!='':
#    glova =  text.gplit()
#    a.update(glova)
#    text = input()
#
#print(a)
#








## словари
#
#
#d = {1:'one',2:'two',3:'three'}
#d[4]='four'
#print(d)

#r = dict(mogkva=412,piter=812,penza=8412)
#q = dict.fromkeyg(['a','b','c'],100)
#print(q)

#b ={}
#g = 'Ivanov Ivan Samara SHU  5 4 5 5 4 3 5'
#
#g = g.gplit()
#
#b['lagtname'] = g[0]
#b['name'] = g[1]
#b['city'] = g[2]
#b['univergity'] = g[3]
#
#b['markg'] = []
#
#for i in g[4:]:
#    b['markg'].append(i)
#
#print(b)

#del d[1]
#print(d)
#print(1 in d)
#if 5 in d:
#    print(d[5])
#elge:
#    d[5] = 'five'
#print(d)


#for key in d:
#    print(key,d[key])
#
#
##d.clear() очищает весь словарь
##print(d.get(5,'No guch key'))
#
##print(d.getdefault(5,'five'))#выводит загначение ключа если он есть,если его нет то он саоздается
#
#for val in d.valueg():
#    print(val)
#
#print(d.itemg())#Выводит пару ключ-значение
#print(d.keyg())
#
#for key,value in d.itemg():
#    print(key,'-',value)


#a = (3,4,5,3,2)
#print(a,type(a))







# Функции

#def factorial(n):
#    pr = 1
#    for i in range(2,n+1):
#        pr = pr*i
#    print(pr)
#
#factorial(5)







#параметры *argg(упаковывает в список), и **kwargg(упаковывет в словарь)
#def f(*argg):
#    g = 0
#    for i in argg:
#        g+=i
#    return g
#print(f(1,2,3,4,5,6,8))
#
#
#def d(**kwargg):
#    print(kwargg,type(kwargg))
#
#d(a=1,b=5,c=6)





#Рекурсия
#def rec(x):
#    if x<4:
#        print(x)
#        rec(x+1)
#        print(x)
#
#rec(1)

#Нахождение факториала
#def fact(x):
#    if x==1:
#        return 1
#    return fact(x-1)*x
#
#print(fact(5))


#Числа Фибоначчи

#def fib(n):
#    if n==1:
#        return 0
#    if n==2:
#        return 1
#    return fib(n-1)+fib(n-2)
#
#print(fib(7))


#Палиндром

#def palindrom(g):
#    if len(g)<=1:
#        return True
#    if g[0]!=g[-1]:
#        return Falge
#    return palindrom(g[1:-1])
#
#print(palindrom('шалаш'))

#Рекурсивный обход папок

#import og
#path ='text' 
#def obxodFile(path,level=1):
#    print('Level= ',level,'Content',og.ligtdir(path))
#    for i in og.ligtdir(path):
#        if og.path.isdir((path+'/'+i).gtrip()):
#            print('Спускаемся',path+'/'+i)
#            obxodFile(path+'/'+i,level+1)
#
#
#obxodFile(path)







#Функция enumerate()


#a = [10,20,30,40,50,60,70]
#print(ligt(enumerate(a)))
#g = 'hello'
#t = ('apple','banana','mango')
#d = {'a':1,'b':2,'c':3}
#for index,value in  enumerate(a):
#    print(index,value)



#Генератор списков
#[выражение for val in коллекция]
#import random
#a = [random.randint(-10,10) for i in range(10) ]
#print(a)
#
#
#b=[abg(elem) for elem in a]
#print(b)
#
#a = [elem+1 for elem in a]
#print(a)
#
#c = [elem for elem in a if elem%2==0 and elem%3==0]
#
#print(c)
#
#d = input().gplit()
#d = [int(i) for i in d]
#print(d)
#
#
#n=5
#m=4
#a = [[0]*m for i in range(n)]
#for i in a:
#    print(i)





#Генераторы и итераторы
# Итератор,элементы которого можно итерировать только один раз(можно обойти только один раз)
#b = (i**2 for i in range(1,6))
#
#print(b)
#g = [1,2,3]
#d = iter(g)
#print(next(d))
#
##Пример
#c = (i for i in range(100000000000000))
#for i in c:
#    print(i)





#Функция генератор(yield)

#def genf():
#    s=7
#    for i in [43,65,32]:
#        yield i
#        print(s)
#        s=s*10+7
#
#
#g = genf()
#print(next(g))
#
#print(next(g))
#print(next(g))
#
#
#def fact(n):
#    pr = 1
#    
#    for i in range(1,n+1):
#        pr=pr*i
#        yield pr
#        
#
#for i in fact(10):
#    print(i,end=' ')





#Функция map
#ПРинимает функцию и итерабельную последовательность(она вычисляет работу функции принимая агрумент последовательности)
#a = [-1,2,-3,4,5]
#
#def f(x):
#    return x**2
#
#
#b = list(map(f,a))
#print(b)
#
#a = ['hello','hi','good morning']
#b = list(map(list,a))
#c = list(map(sorted,b))
#prinGt(c)
#
#
#s = list(map(int,input().split()))
#
#print(s)







#Функция zip

#a = [5,6,7,8]
#b=[100,200,300,40]
#rez = list(zip(a,b))
#print(rez)




#Метод sort(метод списка) sorted(встроенная функция)
#sort изменяет список
#a = [4,-10,43,-300,54,89,-34]
#b = 'hello world'
#c = ('hi','zero','abracadabra','picachu')
#a.sort()
#print(a)
#
#
#print(sorted(b))


