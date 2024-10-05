
from parent import *
from son import *
from classTest import * 

par1 = Parent("parent1","parent2","parent3")
print(par1.parentMethod1())

son11= Son1(par1.atrb1,par1.atrb2,par1.atrb3,"son14","son15","son16")
print(son11.sonMethod1())

print(son11.atrb1)
print(son11.atrb2)
print(son11.atrb3)
print(son11.atrb4)
print(son11.atrb5)
print(son11.atrb6)

print("--------------------------")

test1 = testClass1("A", "B", par1) 

test1.show()
