# Program to illustrate methods in classes


class Employee:
    hike = 1.04

    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    def print_details(self):
        print(self.name)
        print(self.sal)
        print(Employee.hike)

    @classmethod
    def change_hike(cls, hike):
        cls.hike = hike

    @staticmethod
    def is_weekday(day):
        if day == 'Sunday' or day == 'Saturday':
            return False
        return True


emp1 = Employee('Frank', 5000)
emp2 = Employee('Scott', 7000)
emp1.print_details()
Employee.change_hike(1.05)
print(Employee.is_weekday('Sunday'))
