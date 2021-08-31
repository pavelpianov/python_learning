age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))

print('Возраст' + name + ' -- ' + str(age) + ' лет.')

print('Возраст {} -- {} лет.'.format(name, age))

print('Почему {0} забавляется с этим Python?'.format(name))

print('Почему {} забавляется с этим Python?'.format(name))




# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))
#'0.333'

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11}'.format('hello'))
#'___hello___'

# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
#'Swaroop написал A Byte of Python'