from oop import amount_error as er


class SavingsAccount:
    def __init__(self, acno, name, bal):
        self.acno = acno
        self.name = name
        self.bal = bal

    def print_details(self):
        print("Account Number : ", self.acno)
        print("Name           : ", self.name)
        print("Balance        : ", self.bal)

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        try:
            if amount > self.bal:
                raise er.AmountError("Insufficient Balance")
        except Exception as ex:
            print(ex)
        else:
            self.bal -= amount


a = SavingsAccount(1, "Prathek", 1000)
a.withdraw(5000)
a.deposit(5000)
a.withdraw(2000)
a.print_details()








