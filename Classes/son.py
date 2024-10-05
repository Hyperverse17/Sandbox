
from parent import Parent

class Son1(Parent):
    def __init__(self,atrb1,atrb2,atrb3,atrb4,atrb5,atrb6):
        super().__init__(atrb1,atrb2,atrb3)
        self.atrb4 = atrb4
        self.atrb5 = atrb5
        self.atrb6 = atrb6

    def sonMethod1(self):
        return "this is the son 1 method 1"