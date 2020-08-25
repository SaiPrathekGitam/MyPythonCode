# Class to store student details


class Student:
    def set(self, course):
        if course == 'j':
            self.course = "Java"
            self.total = 5000
        elif course == 'p':
            self.course = "Python"
            self.total = 6000
        elif course == 'c':
            self.course = "C++"
            self.total = 4000

    def __init__(self, adm_no, name, course='j', fee_paid=0, total=0):
        self.adm_no = adm_no
        self.name = name
        self.course = course
        self.fee_paid = fee_paid
        self.total = total
        self.set(course)

    def print_details(self):
        print(f"Admission Number = {self.adm_no}")
        print(f"Name     : {self.name}")
        print(f"Course   : {self.course}")
        print(f"Fee Paid : {self.fee_paid}")
        self.balance()

    def payment(self, amount):
        if amount > self.total:
            self.fee_paid = amount
            print(f"Amount Paid is more than Course Fee ({self.total})")
        else:
            self.fee_paid = amount

    def due_amount(self):
        return self.total - self.fee_paid

    def balance(self):
        if self.due_amount() > 0:
            print(f"Fee Due : {self.due_amount()}")
        elif self.due_amount() < 0:
            print(f"Extra Fee Paid : {abs(self.due_amount())}")
        else:
            print("Exact amount of fee has been paid")

    def change(self, course):
        print(f"The Course has changed from {self.course} to ", end="")
        self.set(course)
        print(self.course, "and ", end="")
        self.balance()


s = Student(1234, "Adam", "p")
s.payment(6000)
s.print_details()
s.change("j")
s.print_details()
