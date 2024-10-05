

from datetime import date
class Person:
    def __init__(self,inputName,inputLastName,inputAge):
        self.name     = inputName
        self.lastname = inputLastName
        self.age      = inputAge
        self.birthday = None
    
    def greet(self,inputSomeone):
        greetString = "Hola, "+ inputSomeone + ". Mi nombre es " + self.name + " y tengo " + str(self.age) + " años"
        return greetString
        