
from parent import Parent
parent = Parent("","","")

class testClass1():
    def __init__(self,atrb1,atrb2,parent):
        self.atrb1 = atrb1
        self.atrb2 = atrb2
        self.atrb3 = parent

    def show(self):
        print(self.atrb1)
        print(self.atrb2)
        print(self.atrb3)
