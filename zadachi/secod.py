number = 'asdf'


def sum_of_digit(some_number):
    number_of_digit = str(some_number)
    try:
        arr = [int(i) for i in number_of_digit] 
        summ = 0
        for i in arr:
            summ+=i
        return summ


    except:
        return 'Чё самый умный'
   
print(sum_of_digit(number))
