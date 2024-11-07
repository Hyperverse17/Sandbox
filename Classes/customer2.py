
from bank import Bank
class Customer2(Bank):
    #originBank = Bank("40002","BANAMEX")
    def __init__(self,inputBank,cusID,cusName) -> None:
        self.originBank = inputBank
        self.cusId = cusID
        self.cusName = cusName
        
    