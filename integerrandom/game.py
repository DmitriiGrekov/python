import random

a = random.randint(1,100)


x = 0


while True:

    x = int(input('Угадайте число: '))
    
    if x==a:

        print('Вы угадали')
        break

    elif x>a:

        print('Слишком много')

    else:

        print('Слишком мало')
