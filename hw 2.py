import random

class Student:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 100

    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш рахунок поповнено на {amount} грн. Поточний баланс: {self.balance} грн.')

    def withdraw(self, amount):
        if amount > self.balance:
            print('На балансі недостатньо коштів. Операцію скасовано.')
        else:
            self.balance -= amount
            print(f'З рахунку знято {amount} грн. Поточний баланс: {self.balance} грн.')

    def show_balance(self):
        print(f'Ваш поточний баланс: {self.balance} грн.')

def generate_account_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

account_number = generate_account_number()
print(f'Вітаємо у банку Crocodilo Bombordilo Indastris! Ваш номер рахунку: {account_number}')
user = Student(account_number)

while True:
    action = input('\nВведіть "депозит", "вивід", "баланс" або "вихід" для завершення: ').strip().lower()

    if action == 'депозит':
        try:
            amount = int(input('Введіть суму депозиту: '))
            if amount > 0:
                user.deposit(amount)
            else:
                print('Сума має бути більшою за нуль.')
        except ValueError:
            print('Будь ласка, введіть коректне число.')

    elif action == 'вивід':
        try:
            amount = int(input('Скільки бажаєте зняти? '))
            if amount > 0:
                user.withdraw(amount)
            else:
                print('Сума має бути більшою за нуль.')
        except ValueError:
            print('Будь ласка, введіть коректне число.')

    elif action == 'баланс':
        user.show_balance()

    elif action == 'вихід':
        print('Дякуємо за користування нашими послугами!')
        break

    else:
        print('Невідома команда. Спробуйте ще раз.')
