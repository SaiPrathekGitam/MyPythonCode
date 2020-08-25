# Program to illustrate exception handling


# def add(names):
#     try:
#         names.add('End')
#     except ValueError as ex:
#         names.append('End')


# def addn(names):
#     if isinstance(names, set):
#         names.add('End')
#     else:
#         names.append('End')


# s = {1, 2, 3}
# l = [1, 2, 3]
# addn(s)
# addn(l)
# print(s)
# print(l)

# s = 0
# for i in range(1, 11):
#     try:
#         s += int(input())
#     except ValueError as ex:
#         print(ex)
# print(s)

# s = 0
# i = 0
# while i < 10:
#     try:
#         s += int(input())
#         i += 1
#     except ValueError as ex:
#         print(ex)
# print(s)
class BalanceError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class SavingsAccount:
    def __init__(self, ano, name, bal):
        self.ano = ano
        self.name = name
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        if amount > self.bal:
            raise BalanceError('Idiot')
        self.bal -= amount

    @property
    def get_balance(self):
        return self.bal


sv = SavingsAccount(1, 'Adam', 3000)
sv.withdraw(5000)
