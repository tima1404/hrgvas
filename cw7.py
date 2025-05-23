'''my_list = [1, 2, 3, 4]
for i in range(len(my_list)):
    print(i)'''
from enum import nonmember

'''my_list = [1, 2, 3, 4]
iterator = iter(my_list)
print(next(iterator))
print('Що завгодно')
print(next(iterator))
print('Якийсь код')
print(next(iterator))
print(next(iterator))'''

'''def counter():
    yield 1
    yield 2
    yield 3

gen = counter()
print(next(gen))
print(next(gen))
print(next(gen))'''

'''def counter(start=1, step=1):
    while True:
        yield start
        start += step
gen = counter()
for i in range(5):
    print(next(gen))'''

'''def counter(start=5, step=-1):
    while True:
        yield start
        start += step
gen = counter()
for i in range(5):
    print(next(gen))'''

'''def counter(start=0):
    count = start
    def next_number(step=1):
        nonlocal count
        count += step
        return count
    return next_number()
counter = counter
print (counter(2))'''

'''import tkinter as tk
def counter(start):
    while start >=0:
        yield start
        start -= 1
start_time = 60
counter = counter(start_time)

def update():
    try:
        time_left = next(counter)
        label.config(text=f'Залишилось: {time_left}')
        root.after(1000, update)
    except StopIteration:
        label.config(text='Час вийшов!!!!!!!!!!!!!!!!')

root = tk.Tk()
root.title('Timer')
label = tk.Label(root, font=('Helvetica', 24), fg='blue')
label.pack(padx=20, pady=20)

update()
root.mainloop()
'''

'''def logger(func):
    def wrapper(expression):
        result = func(expression)
        print(f'[LOG] Вираз: {expression} = {result}')
        return result
    return wrapper

def safe_input(func):
    def wrapper(expression):
        allowed = set('0123456789/*-+(). ')
        if not set(expression).issubset(allowed):
            raise ValueError('Неприпустимі символи у виразі')
        return func(expression)
    return wrapper

@logger
@safe_input

def calculate(expression):
    return eval(expression)

while True:
    try:
        expr = input('Введіть вираз: ')
        if expr == 'exit':
            break
        print('Результат: ', calculate(expr))
    except Exception as e:
        print('Помилка:', e)'''

'''import logging
import time

logging.basicConfig(
    filename='log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def divide(a,b):
    logging.info('divide function with arguments: a={a}, b={b}')
    try:
        result = a / b
        logging.info(f'Result: {result}')
        return result
    except ZeroDivisionError as e:
        logging.error('Division by zero!', exc_info=True)
        return None

def test_divide():
    assert divide(10,2) == 5
    assert divide(10,0) is None
    logging.info('Test completed Successfully')


if __name__=='__main__':
    divide(12,6)
    divide(5, 0)
    test_divide()
'''

