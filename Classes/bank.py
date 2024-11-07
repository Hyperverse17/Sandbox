
class Bank():
    bankId    = str
    instName  = str
    instRfc   = str
    constDate = str
    address   = str
    zipCode   = str
    
# Definiendo el Método Constructor (elementos minimos para instanciar objetos)
    def __init__(self,bankId,instName):
        self.bankId    = bankId
        self.instName  = instName
        