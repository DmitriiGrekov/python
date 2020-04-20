import random
import re
arr = open('sowpods.txt','r').read().split()



random_word = random.choices(arr)[0].lower()

x = 10
uncnowing_word = ['_ ' for i in range(0,len(random_word))]
print('У вас 10 жизней')
while x>=0:
    print(uncnowing_word)
    if ''.join(uncnowing_word) == random_word:
        print('Вы выиграли')
        break
    
    word = input('Введите букву: ')
    if word in random_word:
        pos =[m.start() for m in re.finditer(word, random_word)]
        for i in pos:
            uncnowing_word[i] = word


    else:
        if x==0:

            print('Вы проиграли')
            print('Загаданное слово было {0}'.format(random_word))
            break
        else:

            x-=1
            print(f'У вас осталось {x} жизней')

    
        
