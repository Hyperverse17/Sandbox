
from person import Person
class Employee(Person):
    def __init__(self,name,lastname,age,salary):
        super().__init__(name,lastname,age)
        self.salary = salary
        self.salaryFmt = "${:,.2f}".format(self.salary)
        
    def showInfo(self,input):
        if input == "age":
            returnedValue = self.age
        elif input == "name":
            returnedValue = str(self.name) + " " + str(self.lastname)
        elif input == "salary":
            returnedValue = self.salaryFmt
        else:
            returnedValue = "Not Defined"
        
        return returnedValue


        
