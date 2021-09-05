

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


def someFunction():
    '''
    Каждая функция содержит в неявной форме оператор return None в конце, если вы
    не указали своего собственного оператора return. В этом можно убедиться, запустив
    print(someFunction()), где функция someFunction – это какая-нибудь функция, не
    имеющая оператора return в явном виде
    '''
    pass


print(maximum(2, 3))
print(someFunction())
