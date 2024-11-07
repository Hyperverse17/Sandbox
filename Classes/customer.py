
from bank import Bank

class Customer(Bank):
    bankId    = str
    instName  = str
    cusId     = str
    cusName   = str
    cusBirthDay  = str
    cusLastName1 = str
    cusLastName2 = str
    def __init__(self, bankId, instName, cusId, cusName, cusLastName1):
        super().__init__(bankId, instName)
        self.cusId     = cusId
        self.cusName   = cusName
        self.cusLastName1 = cusLastName1
