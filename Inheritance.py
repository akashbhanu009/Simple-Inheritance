class Engine:
    a=10

    def __init__(self):
        self.b=20

    def m1(self):
        print("This is engine class method m1()")
class car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print("This is another class car which inherite the properties of class Engine")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c = car()
c.m2()
