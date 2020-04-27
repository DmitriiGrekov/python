# -*- coding: utf-8 -*-



s = 'adklfjxzkasdjfqwkljwkljnvxz' 




if 'x' in s and 'w' in s:
    x=s.index('x')
    w=s.index('w')

    if x==0:
        print('Х встречается первее')


    elif w==0:
        print('W встречается первее')
    elif x>w:
        print('W встречается первее')


    else:
        print('Х встречается первее')
else:
    print('Нет этих букв')
