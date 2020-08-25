# Student class

class Student:
    def __init__(self, ano, name, course='j', fee=0):
        self.ano = ano
        self.name = name
        self.course = course
        self.fee = fee
        self.paid = 0

    def set_course(self, course):
        self.course = course
        print('Course Changed To', self.course)
        if course == 'j':
            self.fee = 5000
        elif course == 'p':
            self.fee = 6000
        else:
            self.fee = 5000
        if self.due_amount() < 0:
            self.refund()

    def print_details(self):
        print('Admission Number :', self.ano)
        print('Name :', self.name)
        print('Course :', self.course)
        print('Fee :', self.fee)
        print('Amount Due :', self.due_amount())

    def payment(self, amount):
        if amount <= self.due_amount():
            self.paid += amount
            print('Paid Amount', amount)
            print('Due Amount : ', self.due_amount())
        else:
            print('Amount Exceeds Due Amount : ', self.due_amount())

    def refund(self):
        print('Amount Refunded : ', -self.due_amount())
        self.paid += self.due_amount()

    def due_amount(self):
        return self.fee - self.paid


s = Student(1, 'Prathek')
s.set_course('p')
s.print_details()
s.payment(6000)
s.set_course('c')
