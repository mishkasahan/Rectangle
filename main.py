class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def ploshtha(self):
        return self.a*self.b

    def perymetr(self):
        return 2*(self.a+self.b)


prjamok1 = Rectangle(2,5)
print(prjamok1.perymetr())
print(prjamok1.ploshtha())