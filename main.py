try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = num_1 / num_2
except ValueError:
    print('Введен неверный тип данных')
except ZeroDivisionError:
    int(input('Введите первое число заново: '))
    int(input('Введите второе число заново: '))
except Exception:
    print('Общее исключение')
else:
    print(f'резуьтат:  {num_3}')


