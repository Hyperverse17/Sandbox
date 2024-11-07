
from bank import Bank
from customer import Customer
from customer2 import Customer2
from account import Account

b40113 = Bank("40113","VE POR MAS")

b40113.address = "Reforma 241"

print(b40113.bankId)
print(b40113.instName)
print(b40113.address)

c40113001 = Customer(b40113.bankId, b40113.instName, "001", "Otelo", "Galicia")

c40113001.cusBirthDay = "19910717"

print(c40113001.instName)
print(c40113001.cusId)
print(c40113001.cusName)
print(c40113001.cusLastName1)
print(c40113001.cusBirthDay)

a40113001001 = Account(b40113.bankId, b40113.instName, c40113001.cusId, c40113001.cusName, c40113001.cusLastName1, "001", "Nomina", "20241011")

print("---")


customer002 = Customer2(b40113,"001","Valeria")

print(customer002.bankId)
print(customer002.bankName)
