# Program to illustrate MRO


class A:
    def call(self):
        self
        print('In A')


class B(A):
    pass
    # def call(self):
    #     self
    #     print('In B')


class C(A):
    def call(self):
        self
        print('In C')


class D(B, C):
    pass
    # def call(self):
    #     self
    #     print('In D')


obj = D()
obj.call()
