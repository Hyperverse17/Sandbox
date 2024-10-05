
from datetime import date
from person import *
from employee import *

person1 = Person("Otelo","Galicia",33)
person1.birthday = date(1991,7,17)

person2 = Person("Miguel","Garcia",50)

greet = person1.greet("Paco")
print(greet)
print(person1.birthday)

emp1 = Employee("Mariana","Gomez", 30, 30000)

print()
print(emp1.showInfo("salary"))
print(emp1.showInfo("name"))
print(emp1.showInfo("age"))
print(emp1.showInfo("something"))

emp2 = Employee(person1.name,person1.lastname,person1.age,10000)

print()
print(emp2.showInfo("salary"))
print(emp2.showInfo("name"))
print(emp2.showInfo("age"))
print(emp2.showInfo(""))

emp3 = Employee(person2.name,person2.lastname,person2.age,20000)
print()
print(emp3.showInfo("salary"))
print(emp3.showInfo("name"))
print(emp3.showInfo("age"))
print(emp3.showInfo(""))