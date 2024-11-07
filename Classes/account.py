

from customer import Customer

class Account(Customer):
    accWorkingBalence = float
    def __init__(self, bankId, instName, cusId, cusName, cusLastName1, accId, accType, accOpeningDate):
        super().__init__(bankId, instName, cusId, cusName, cusLastName1)
        self.accId = accId
        self.accType = accType
        self.accOpeningDate = accOpeningDate